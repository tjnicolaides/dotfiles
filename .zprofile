# echo "Arch: $(arch)"
eval "$(/opt/homebrew/bin/brew shellenv)"
for file in ~/.{extra,bash_prompt,exports,aliases,functions,bashrc}; do
        [ -r "$file" ] && source "$file"
done
unset file

export PATH="/Users/$(whoami)/bin:$PATH"
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"

# Added by Toolbox App
export PATH="$PATH:/Users/tj_nicolaides/Library/Application Support/JetBrains/Toolbox/scripts"
# AIRLAB-DO-NOT-MODIFY section:ShellWrapper {{{
# Airlab will only make edits inside these delimiters.

# Source Airlab's shell integration, if it exists.
if [ -e ~/.airlab/shellhelper.sh ]; then
  source ~/.airlab/shellhelper.sh
fi
# AIRLAB-DO-NOT-MODIFY section:ShellWrapper }}}
