#!/usr/bin/env bash
# Restore all demo materials to their pre-talk state.
# Pristine content comes from the talk repo's last commit — commit before resetting.
set -euo pipefail
cd "$(dirname "$0")"
ROOT="$(git rev-parse --show-toplevel)"

# Safety: abort if HEAD still records the demo dirs as embedded repos (gitlinks)
for d in messy-project ruff-demo vim-demo; do
  mode="$(git -C "$ROOT" ls-tree HEAD "demo/$d" | awk '{print $1}')"
  if [ "$mode" = "160000" ]; then
    echo "error: demo/$d is still an embedded repo in HEAD." >&2
    echo "       Commit the plain files first (see demo/README.md), then re-run." >&2
    exit 1
  fi
done

git -C "$ROOT" checkout -q HEAD -- demo/messy-project demo/ruff-demo demo/vim-demo
./setup.sh
echo "All demos reset."
