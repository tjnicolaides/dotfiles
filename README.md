# Dotfiles

My personal dotfiles, managed with a Git bare repository.

## How It Works

This setup uses a Git bare repository stored in `~/.dotfiles` to track configuration files in the home directory, based on [this tutorial](https://web.archive.org/web/20240307132655/https://engineeringwith.kalkayan.com/series/developer-experience/storing-dotfiles-with-git-this-is-the-way/).

## Setup

```bash
# Clone the bare repository
git clone --bare https://github.com/USERNAME/dotfiles.git $HOME/.dotfiles

# Define the alias in the current shell
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'

# Checkout the actual content
dotfiles checkout

# Hide untracked files
dotfiles config --local status.showUntrackedFiles no
```

## Usage

Instead of using the `git` command, use the `dotfiles` alias to manage your configuration:

```bash
# Check status
dotfiles status

# Add a file
dotfiles add .vimrc

# Commit changes
dotfiles commit -m "Add vimrc"
```

## Tracked Files
- `.aliases` - Custom shell aliases
- `.gitconfig` - Git configuration
- `.gitignore_global` - Global Git ignore patterns
- `.zprofile`
- `.zshrc` 




