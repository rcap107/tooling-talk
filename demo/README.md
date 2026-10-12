# Live demo materials

Run-of-show for the demos in `index.qmd`. Rehearse once with `reset.sh` at the start.

| # | Slide | Dir | Beat |
|---|-------|-----|------|
| 1 | Shell: fzf + zoxide | `shell-config/` | `Ctrl+R` history → `z proj` → `Ctrl+T` file pick with bat preview (`zshrc.snippet.zsh`) |
| 2 | ripgrep + bat | `messy-project/` | `grep` (slow) vs `rg` · `--count` · `--no-ignore` finds the needle in `data/` |
| 3 | tmux | `tmux-demo/` | split panes + `tail -f`, detach, close terminal, reattach — job alive |
| 4 | uv / pixi | `uv-pixi/` | `uv init` + `uv add` live; show `pixi.toml` + lockfile |
| 5 | ruff | `ruff-demo/` | `ruff check .` → `--fix` + `format` → `git diff` = readable |
| 6 | vim | `vim-demo/` | 3 bugs revealed one by one; fixes = `ci"`, `dd`+`p`, `2dd` (`answer-key.md`) |
| 7 | Quarto meta-demo | `../index.qmd` | edit a bullet live, re-render; roadmap diagram is Mermaid text |

## Before the talk / after cloning

```bash
./setup.sh    # creates the throwaway git repos demos 2 and 5 need
```

## Reset everything (between rehearsals)

```bash
./reset.sh   # restores demo files from the talk repo's last commit, then re-runs setup.sh
```

The inner `.git` repos created by `setup.sh` are **build artifacts** — never commit
them. If `git status` ever shows `demo/<dir>` as an embedded repo, you've committed
one: `git rm -r --cached demo/<dir> && git add demo/`.

## Demo 6 answer key (do not project)

See `vim-demo/answer-key.md`. Sequence: `FileNotFoundError` → `ci"`;
`NameError: late_pct` → `dd` + `k` + `p`; `DEBUG` spam → `2dd`.
