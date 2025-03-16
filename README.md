# My Config files (dotfiles, nvim, etc.)

## Requirements:
- GNU stow (otherwise manual symlink)
- tmux v3.4 (otherwise ERROR: `invalid option: allow-passthrough`)

## Dotfiles
For simplest setup clone to `$HOME/.dotfiles` (i.e. clone in `~` dir)
- Run `stow shell` from repo root
- To remove configs run `stow -D shell` from repo root

If cloned elsewhere:
- Run `stow -t $HOME shell` from repo root
- To remove configs run `stow -Dt $HOME shell` from repo root

## Env and Dependencies
### Pre
- `sudo apt update`

### GNU Stow (manage dotfiles)
- `sudo apt install -y stow`

### Build Tools (to install (build) programs with cargo)
- `sudo apt install -y build-essential cmake`

### Tmux (Terminal multiplexer/window manager)
- `sudo apt install -y tmux`
- Install [plugin manager](https://github.com/tmux-plugins/tpm):
`git clone https://github.com/tmux-plugins/tpm $HOME/.tmux/plugins/tpm`

### Zsh Highlighting (For "Fish-like" syntax hightlighting)
- Install [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting):
`git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.zsh/plugins/zsh-syntax-highlighting`

## Additional Env setup
### GitHub CLI
- Install [gh](https://github.com/cli/cli/blob/trunk/docs/install_linux.md):
```
(type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y
```
- Login: `gh auth login`

### Python
- Install [pip](https://pip.pypa.io/en/stable/installation/#get-pip-py):
`curl -sS https://bootstrap.pypa.io/get-pip.py | python3`
- Install [pyenv](https://github.com/pyenv/pyenv):
`git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv`
- Setup env for [pyenv](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
(required to run `pyenv install x.x.x`):
```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
