#!/usr/bin/env bash
# Setup script for claude.ai/code cloud environments. Installs this repo's Claude
# config into ~/.claude so CLAUDE.md, skills and agents load in every session:
#   curl -fsSL https://raw.githubusercontent.com/tjnicolaides/dotfiles/main/.claude/scripts/cloud-bootstrap.sh | bash
set -euo pipefail

src=$(mktemp -d)
git clone -q --depth 1 https://github.com/tjnicolaides/dotfiles "$src"
mkdir -p "$HOME/.claude"
cp -rn "$src/.claude/." "$HOME/.claude/"
rm -rf "$src"

# The ai-writing plugin is hosted on a work-only git server.
python3 - "$HOME/.claude/settings.json" <<'PY'
import json, sys
path = sys.argv[1]
with open(path) as f:
    settings = json.load(f)
settings.get("enabledPlugins", {}).pop("writing@ai-writing", None)
settings.get("extraKnownMarketplaces", {}).pop("ai-writing", None)
with open(path, "w") as f:
    json.dump(settings, f, indent=2)
PY
