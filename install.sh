# install nix
curl -L https://nixos.org/nix/install | sh

# source nix
. ~/.nix-profile/etc/profile.d/nix.sh

# install packages
nix-env -iA \
	nixpkgs.fish \
    nixpkgs.oh-my-fish\
	nixpkgs.git \
	nixpkgs.neovim \
	nixpkgs.tmux \
	nixpkgs.stow \
	nixpkgs.yarn \
	nixpkgs.fzf \
	nixpkgs.ripgrep \
	nixpkgs.bat \
	nixpkgs.gcc \

# stow dotfiles
stow git
stow nvim
stow tmux
stow fish
stow omf

# add fish as a login shell
command -v fish | sudo tee -a /etc/shells

# use fish as default shell
sudo chsh -s $(which fish) $USER
