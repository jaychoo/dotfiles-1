#!/bin/bash

echo "####### installing homebrew"
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

echo "####### installing git"
brew install git

echo "####### bootstrapping ghar"
git clone https://github.com/jacobian/ghar.git .ghar
.ghar/bin/ghar add https://github.com/jacobian/dotfiles.git
.ghar/bin/ghar add https://github.com/jacobian/dotfiles-private.git
.ghar/bin/ghar install

echo "####### homebrewing the world"
./.brew

echo "####### python"
pip install -U pip
pip install -r .requirements.txt

echo "####### fixing osx"
./.osx
