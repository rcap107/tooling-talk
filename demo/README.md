# Live demo materials

Run-of-show for the demos in `index.qmd`. Rehearse once with `reset.sh` at the start.

| # | Slide | Dir | Beat |
|---|-------|-----|------|
| 1 | Shell: fzf + zoxide | `shell-config/` | `Ctrl+R` history → `z proj` → `Ctrl+T` file pick with bat preview (`zshrc.snippet.zsh`) |
| 2 | ripgrep + bat | `messy-project/` | `grep` (slow) vs `rg` · `--count` · `--no-ignore` finds the needle in `data/` |
| 3 | tmux | `tmux-demo/` | split panes + `tail -f`, detach, close terminal, reattach — job alive |
| 4 | uv / pixi | `uv-pixi/` | `uv init` + `uv add` live; show `pixi.toml` + lockfile |
| 5 | ruff | `ruff-demo/` | `ruff check .` → `--fix` + `format` → `git diff` = readable |
| 6 | git tags | `git-tags/` | edit lr → rerun → commit → `git diff v1.0-baseline HEAD` |
| 7 | vim | `vim-demo/` | 3 bugs revealed one by one; fixes = `ci"`, `dd`+`p`, `2dd` (`answer-key.md`) |

## Per-demo reset (or use `./reset.sh` for all)

```bash
git -C ruff-demo checkout .                 # demo 5
./git-tags/setup.sh                         # demo 6 (after rm -rf git-tags/.git)
git -C vim-demo checkout .                  # demo 7
git -C messy-project checkout . && git -C messy-project clean -fd   # demo 2
```

## Demo 7 answer key (do not project)

See `vim-demo/answer-key.md`. Sequence: `FileNotFoundError` → `ci"`;
`NameError: late_pct` → `dd` + `k` + `p`; `DEBUG` spam → `2dd`.
