# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# History settings
HISTFILE=$HOME/.zsh_history
HISTSIZE=100000
SAVEHIST=1000000

setopt inc_append_history        # Append history to the file as it is created
setopt share_history             # Share history across multiple shell sessions
setopt hist_ignore_all_dups      # Ignore duplicate entries in history
setopt hist_save_no_dups         # Do not save duplicate entries
setopt extended_history          # Save timestamps in the history file
setopt hist_expire_dups_first    # Remove duplicates first if history size exceeds limit

export LANG=ja_JP.UTF-8


# Python
alias py='python'

# atcoder
# vscode
alias vs='code -r main.py'
# cd
for d in {a..g}; do
  alias $d="cd ../$d ; vs"
done
alias test='oj test -c "python main.py" -d ./tests/ -N -D'
alias contest="source init_contest.sh"
alias practice="source init_practice.sh"
alias sd='source submit.sh'
alias sf='source submit_safe.sh'

# Shell option settings
setopt auto_param_keys      # Auto complete for key-value pairs
setopt auto_cd              # Auto cd to directories without 'cd' command
setopt correct              # Spell correction for commands
setopt correct_all          # Spell correction for full command line
setopt auto_param_slash     # Auto add '/' at end of directories
setopt mark_dirs            # Mark directories with '/'
setopt auto_menu            # Auto menu completion for repeated key press
setopt interactive_comments # Treat '#' as comments
setopt magic_equal_subst    # Expand variables in arguments like --prefix=$HOME
setopt complete_in_word     # Complete at cursor position
setopt print_eight_bit      # Enable displaying Japanese characters in file names


# 色の設定
export LSCOLORS=Exfxcxdxbxegedabagacad
export LS_COLORS='di=01;34:ln=01;35:so=01;32:ex=01;31:bd=46;34:cd=43;34:su=41;30:sg=46;30:tw=42;30:ow=43;30'
autoload -Uz colors
colors
zstyle ':completion:*' list-colors "${LS_COLORS}"

PROMPT="%F{green}%n%f %F{cyan}%f:%F{blue}%~%f"$'\n'"%# "


alias lst='ls -ltr --color=auto'
alias ls='ls --color=auto'
alias la='ls -la --color=auto'
alias ll='ls -l --color=auto'
alias mkdir='mkdir -p'

# zsh completion settings
zstyle ':completion:*:commands' rehash 1
zstyle ':completion:*:default' menu select=2
zstyle ':completion:*' matcher-list '' 'm:{[:lower:]}={[:upper:]}' '+m:{[:upper:]}={[:lower:]}'
zstyle ':completion:*' format '%B%F{blue}%d%f%b'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"


# コマンドを途中まで入力後、historyから絞り込み
autoload -Uz history-search-end
zle -N history-beginning-search-backward-end history-search-end
zle -N history-beginning-search-forward-end history-search-end
bindkey "^P" history-beginning-search-backward-end
bindkey "^N" history-beginning-search-forward-end


# Load a few important annexes, without Turbo
# (this is currently required for annexes)
zinit light-mode for \
    zdharma-continuum/zinit-annex-as-monitor \
    zdharma-continuum/zinit-annex-bin-gem-node \
    zdharma-continuum/zinit-annex-patch-dl \
    zdharma-continuum/zinit-annex-rust

### End of Zinit's installer chunk
# zinit ice depth=1; zinit light romkatv/powerlevel10k

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
zinit light zsh-users/zsh-autosuggestions
zinit light marlonrichert/zsh-autocomplete
zinit light mollifier/anyframe

# 追記
zinit ice as"program" from"gh-r" mv"bat* -> bat" pick"bat/bat"
# zinit light sharkdp/bat

# 以下はただのエイリアス設定
if builtin command -v bat > /dev/null; then
  alias cat="bat"
fi

# ディレクトリ移動履歴
bindkey '^xb' anyframe-widget-cdr
autoload -Uz chpwd_recent_dirs cdr add-zsh-hook
add-zsh-hook chpwd chpwd_recent_dirs
