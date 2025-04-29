# .zprofile - Executed for login shells before .zshrc

# Load Homebrew for macOS (ARM64/Apple Silicon)
# Adds Homebrew to your PATH and sets up the environment
eval "$(/opt/homebrew/bin/brew shellenv)"

# Source additional configuration files if they exist
# This loads personal customizations from various dot files
for file in ~/.{extra,bash_prompt,exports,aliases,functions,bashrc}; do
        [ -r "$file" ] && source "$file"
done
unset file

# Add personal bin directory to PATH for custom executables
export PATH="/Users/$(whoami)/bin:$PATH"

# Java environment setup with jenv
# Manages multiple Java versions
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"

# Added by JetBrains Toolbox App
# Adds JetBrains IDE scripts to PATH
export PATH="$PATH:/Users/tj_nicolaides/Library/Application Support/JetBrains/Toolbox/scripts"

# AIRLAB-DO-NOT-MODIFY section:ShellWrapper {{{
# Airlab will only make edits inside these delimiters.

# Source Airlab's shell integration, if it exists.
if [ -e ~/.airlab/shellhelper.sh ]; then
  source ~/.airlab/shellhelper.sh
fi
# AIRLAB-DO-NOT-MODIFY section:ShellWrapper }}}

# Add Visual Studio Code (code)
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
