NEWLINE=$'\n'
PREVIOUS_RESULT="%(?.%F{green}√.%F{red}?%?)%f"
PROMPT='%(?.%F{green}√.%F{red}?%?)%f %F{9}$USER%f %F{240}at%f %F{208}%m%f %F{240}in%f %B%F{136}%~%f%b ${NEWLINE} %F{240}\$%f '

autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst
RPROMPT=\$vcs_info_msg_0_
zstyle ':vcs_info:git:*' formats '%F{141} %b'
zstyle ':vcs_info:*' enable git

# cd to airlab repos dir if it exists
if [ -e ~/airlab/repos ]; then
  cd ~/airlab/repos
fi

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
PATH=$(pyenv root)/shims:$PATH
eval "$(pyenv init -)"
eval "$(pyenv init --path)"

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"


# Homebrew x86_64 version
# If you come from bash you might have to change your $PATH. We need this for x86_64 brew
export PATH=$HOME/bin:/usr/local/bin:$PATH
# For Intel x86_64 brew
alias axbrew="arch -x86_64 /usr/local/homebrew/bin/brew"

if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi

export OPT_OUT_LINT_PRE_PUSH_HOOK=true
export ANDROID_HOME=${HOME}/Library/Android/sdk
export PATH=${PATH}:${ANDROID_HOME}/tools
export PATH=${PATH}:${ANDROID_HOME}/platform-tools
