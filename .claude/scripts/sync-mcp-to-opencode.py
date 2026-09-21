#!/usr/bin/env python3
"""Sync MCP server definitions from Claude Code config into opencode config.

Claude Code is the source of truth (~/.claude.json for global servers, plus
each project's mcpServers block). This script updates the "mcp" key in the
matching opencode config so both tools point at the same servers, without
touching servers the user defined directly in opencode.

Usage:
    ./sync-mcp-to-opencode.py                 # sync global servers only
    ./sync-mcp-to-opencode.py --project PATH  # also sync PATH's project servers
"""
import json
import sys
import tempfile
from pathlib import Path

CLAUDE_JSON = Path.home() / ".claude.json"
GLOBAL_OPENCODE = Path.home() / ".config" / "opencode" / "opencode.jsonc"
MANAGED_MARKER = "_syncedFromClaude"


def strip_comments(text):
    """Strip // and /* */ comments, string-aware (URLs like https:// survive)."""
    out = []
    i, n = 0, len(text)
    in_string = False
    escape = False
    while i < n:
        c = text[i]
        if in_string:
            out.append(c)
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_string = False
            i += 1
            continue
        if c == '"':
            in_string = True
            out.append(c)
            i += 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "/":
            while i < n and text[i] not in "\r\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue
        out.append(c)
        i += 1
    return "".join(out)


def strip_trailing_commas(text):
    """Drop commas right before a closing } or ], string-aware."""
    result = []
    i, n = 0, len(text)
    in_string = False
    escape = False
    while i < n:
        c = text[i]
        if in_string:
            result.append(c)
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_string = False
            i += 1
            continue
        if c == '"':
            in_string = True
            result.append(c)
            i += 1
            continue
        if c == ",":
            j = i + 1
            while j < n and text[j] in " \t\r\n":
                j += 1
            if j < n and text[j] in "}]":
                i += 1
                continue
        result.append(c)
        i += 1
    return "".join(result)


def load_jsonc(path):
    if not path.exists():
        return {"$schema": "https://opencode.ai/config.json"}
    text = path.read_text()
    without_comments = strip_comments(text)
    if without_comments != text:
        print(
            f"warning: {path} has comments; they'll be lost on rewrite",
            file=sys.stderr,
        )
    return json.loads(strip_trailing_commas(without_comments))


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with open(fd, "w") as f:
            f.write(text)
        Path(tmp_path).replace(path)
    except BaseException:
        Path(tmp_path).unlink(missing_ok=True)
        raise


def claude_to_opencode_server(cfg):
    """Convert one Claude mcpServers entry to opencode's mcp entry."""
    if "url" in cfg:
        out = {"type": "remote", "url": cfg["url"]}
        if "headers" in cfg:
            out["headers"] = cfg["headers"]
    else:
        command = [cfg["command"]] + list(cfg.get("args", []))
        out = {"type": "local", "command": command}
        if cfg.get("env"):
            out["environment"] = cfg["env"]
    out[MANAGED_MARKER] = True
    return out


def sync(claude_servers, opencode_path):
    opencode_cfg = load_jsonc(opencode_path)
    mcp = opencode_cfg.setdefault("mcp", {})

    desired_names = set(claude_servers)
    for name, cfg in claude_servers.items():
        new_entry = claude_to_opencode_server(cfg)
        existing = mcp.get(name)
        if isinstance(existing, dict) and existing.get(MANAGED_MARKER):
            # preserve opencode-only fields (enabled, timeout, etc.) that
            # we don't manage, only overwrite the ones we own.
            merged = dict(existing)
            merged.update(new_entry)
            mcp[name] = merged
        elif existing is None:
            mcp[name] = new_entry
        else:
            # user-defined entry with the same name and no marker: leave it
            # alone rather than clobber a manual config.
            print(
                f"skipping {name!r}: exists in opencode config and wasn't "
                "added by this script",
                file=sys.stderr,
            )

    # prune servers we previously synced that Claude no longer has
    for name in list(mcp):
        entry = mcp[name]
        if (
            isinstance(entry, dict)
            and entry.get(MANAGED_MARKER)
            and name not in desired_names
        ):
            del mcp[name]

    atomic_write(opencode_path, json.dumps(opencode_cfg, indent=2) + "\n")
    print(f"synced {len(claude_servers)} server(s) -> {opencode_path}")


def main():
    if not CLAUDE_JSON.exists():
        print("no ~/.claude.json found, skipping")
        return
    claude_cfg = json.loads(CLAUDE_JSON.read_text())

    global_servers = claude_cfg.get("mcpServers", {})
    if global_servers or GLOBAL_OPENCODE.exists():
        sync(global_servers, GLOBAL_OPENCODE)
    else:
        print("no global mcpServers in ~/.claude.json")

    if "--project" in sys.argv:
        idx = sys.argv.index("--project")
        if idx + 1 >= len(sys.argv):
            print("usage: sync-mcp-to-opencode.py --project PATH", file=sys.stderr)
            sys.exit(1)
        project_arg = Path(sys.argv[idx + 1]).expanduser()
        # try the literal (possibly symlinked) path first, since Claude
        # stores project keys as the cwd it was launched from -- falling
        # back to the resolved path if that's what's recorded instead.
        candidates = [str(project_arg), str(project_arg.resolve())]
        projects = claude_cfg.get("projects", {})
        project_path = next((c for c in candidates if c in projects), candidates[0])
        project_servers = projects.get(project_path, {}).get("mcpServers", {})
        opencode_path = Path(project_path) / "opencode.jsonc"
        if not project_servers and not opencode_path.exists():
            print(f"no mcpServers for project {project_path}")
            return
        print(
            f"warning: {opencode_path} may contain secrets (env vars, "
            "headers) -- make sure it's gitignored before committing",
            file=sys.stderr,
        )
        sync(project_servers, opencode_path)


if __name__ == "__main__":
    main()
