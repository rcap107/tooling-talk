#!/usr/bin/env bash
# (Re)create the throwaway git repos that demos 2 and 5 need at runtime.
# The demo content is tracked as plain files in the talk repo; these inner
# repos are build artifacts — never commit them.
set -euo pipefail
cd "$(dirname "$0")"

ensure_identity() {
  git config user.email >/dev/null 2>&1 || git config user.email "speaker@demo.local"
  git config user.name  >/dev/null 2>&1 || git config user.name "Speaker"
}

init_repo() {
  local dir="$1" msg="$2"
  if [ ! -d "$dir/.git" ]; then
    git -C "$dir" init -q
    ( cd "$dir" && ensure_identity && git add -A && git commit -qm "$msg" )
  fi
}

# Demo 2 — messy-project: repo + an uncommitted tweak for the `git diff | bat` beat
init_repo messy-project "Initial (messy) state"
grep -q "TODO(live)" messy-project/src/train.py \
  || printf '\n# TODO(live): remove this line during the demo\n' >> messy-project/src/train.py

# Demo 5 — ruff-demo: repo so the demo can end with `git diff`
init_repo ruff-demo "Ugly initial state"

echo "Demo repos ready."
