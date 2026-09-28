# ~/.zshrc — the parts shown in Demo 1

# --- fzf: fuzzy finder -------------------------------------------------
# modern fzf (0.48+): enables Ctrl-R / Ctrl-T / Alt-C
eval "$(fzf --zsh)"

# Ctrl-T lists files your project actually has (respects .gitignore)
export FZF_DEFAULT_COMMAND='rg --files --hidden --glob "!.git/"'

# Ctrl-T preview: show the highlighted file with bat
export FZF_CTRL_T_OPTS="
  --preview 'bat --color=always --style=numbers --line-range :300 {}'
  --preview-window 'right,60%,border-left'
  --bind 'ctrl-/:change-preview-window(right,60%,border-left|hidden|)'"

# --- zoxide: smarter cd -----------------------------------------------
eval "$(zoxide init zsh)"    # usage: z <partial-directory-name>

# --- aliases ------------------------------------------------------------
alias ll='ls -lah'
alias python='python3'
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline -10'
