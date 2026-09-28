#!/usr/bin/env bash
# Restore all demo materials to their pre-talk state.
set -euo pipefail
cd "$(dirname "$0")"

# ruff-demo: restore ugly.py to its committed ugly state
git -C ruff-demo checkout -q .

# git-tags: wipe and rebuild fresh (recreates baseline commit + tag)
rm -rf git-tags/.git git-tags/results.txt
./git-tags/setup.sh >/dev/null

# vim-demo: restore the buggy state
git -C vim-demo checkout -q .

# messy-project: discard edits + the live TODO line, drop stray files
git -C messy-project checkout -q .
git -C messy-project clean -qfd

echo "All demos reset."
