#!/usr/bin/env python3
"""Sync MCP server definitions from Claude Code config into opencode config.

Claude Code is the source of truth (~/.claude.json for global servers, plus
each project's mcpServers block). This script regenerates the "mcp" key in
the matching opencode config so both tools point at the same servers.

Usage:
    ./sync-mcp-to-opencode.py                 # sync global servers only
    ./sync-mcp-to-opencode.py --project PATH  # also sync PATH's project servers
"""
import json
import re
import sys
from pathlib import Path

CLAUDE_JSON = Path.home() / ".claude.json"
GLOBAL_OPENCODE = Path.home() / ".config" / "opencode" / "opencode.jsonc"


def load_jsonc(path):
    if not path.exists():
        return {"$schema": "https://opencode.ai/config.json"}
    text = path.read_text()
    # strip // line comments (opencode.jsonc allows them; json.loads doesn't)
    stripped = re.sub(r"(?m)^\s*//.*$", "", text)
    return json.loads(stripped)


def claude_to_opencode_server(name, cfg):
    """Convert one Claude mcpServers entry to opencode's mcp entry."""
    if "url" in cfg:
        out = {
            "type": "remote",
            "url": cfg["url"],
        }
        if "headers" in cfg:
            out["headers"] = cfg["headers"]
        return out

    command = [cfg["command"]] + list(cfg.get("args", []))
    out = {
        "type": "local",
        "command": command,
    }
    if cfg.get("env"):
        out["environment"] = cfg["env"]
    return out


def sync(claude_servers, opencode_path):
    opencode_cfg = load_jsonc(opencode_path)
    mcp = opencode_cfg.setdefault("mcp", {})
    for name, cfg in claude_servers.items():
        mcp[name] = claude_to_opencode_server(name, cfg)
    opencode_path.parent.mkdir(parents=True, exist_ok=True)
    opencode_path.write_text(json.dumps(opencode_cfg, indent=2) + "\n")
    print(f"synced {len(claude_servers)} server(s) -> {opencode_path}")


def main():
    if not CLAUDE_JSON.exists():
        print("no ~/.claude.json found, skipping")
        return
    claude_cfg = json.loads(CLAUDE_JSON.read_text())

    global_servers = claude_cfg.get("mcpServers", {})
    if global_servers:
        sync(global_servers, GLOBAL_OPENCODE)
    else:
        print("no global mcpServers in ~/.claude.json")

    if "--project" in sys.argv:
        idx = sys.argv.index("--project")
        project_path = str(Path(sys.argv[idx + 1]).expanduser().resolve())
        project_servers = (
            claude_cfg.get("projects", {}).get(project_path, {}).get("mcpServers", {})
        )
        if not project_servers:
            print(f"no mcpServers for project {project_path}")
            return
        opencode_path = Path(project_path) / "opencode.jsonc"
        sync(project_servers, opencode_path)


if __name__ == "__main__":
    main()
