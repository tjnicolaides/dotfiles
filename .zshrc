# Load secrets (API keys etc) — files are not tracked in git
for _secret_file in ~/.secrets-*(N); do
  [ -r "$_secret_file" ] && source "$_secret_file"
done
unset _secret_file

# Z-Shell configuration file that runs for each interactive shell session
# Custom prompt configuration with color formatting and status indicators
NEWLINE=$'\n'
PREVIOUS_RESULT="%(?.%F{green}√.%F{red}?%?)%f"
PROMPT='%(?.%F{green}√.%F{red}?%?)%f %F{9}$USER%f %F{240}at%f %F{208}%m%f %F{240}in%f %B%F{136}%~%f%b ${NEWLINE} %F{240}\$%f '

# Version control system information setup (shows git branch in prompt)
autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst
RPROMPT=\$vcs_info_msg_0_
zstyle ':vcs_info:git:*' formats '%F{141} %b'
zstyle ':vcs_info:*' enable git

# Workspace initialization - automatically cd to work directory if it exists
if [ -e ~/airlab/repos ]; then
  cd ~/airlab/repos
fi

# Node Version Manager configuration
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Python environment configuration with pyenv
PATH=$(pyenv root)/shims:$PATH
eval "$(pyenv init -)"
eval "$(pyenv init --path)"

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Java environment configuration with jenv
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"

# Homebrew configuration for both Apple Silicon and Intel architectures
# If you come from bash you might have to change your $PATH. We need this for x86_64 brew
export PATH=$HOME/bin:/usr/local/bin:$PATH
# For Intel x86_64 brew
alias axbrew="arch -x86_64 /usr/local/homebrew/bin/brew"

# Ruby environment configuration
if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi

# Development environment configurations
export OPT_OUT_LINT_PRE_PUSH_HOOK=true

# Android development environment setup
export ANDROID_HOME=${HOME}/Library/Android/sdk
export PATH=${PATH}:${ANDROID_HOME}/tools
export PATH=${PATH}:${ANDROID_HOME}/platform-tools

max_files_soft_limit=$(launchctl limit maxfiles | awk 'NR==1 { print $2 }')
if (( max_files_soft_limit <= 1000000 )); then
  echo "Max files soft limit is too low. Running sudo launchctl limit maxfiles 1048576. Please type your Laptop password to run this command as root is required"
  sudo launchctl limit maxfiles 1048576
fi
export PATH="$HOME/.local/bin:$PATH"
