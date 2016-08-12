#!/usr/bin/env bash

sudo apt-get install zsh vim lynx

# oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
# vimrc
git clone git://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_basic_vimrc.sh
# sh ~/.vim_runtime/install_awesome_vimrc.sh

echo Install python packages...
sudo pip3 install -r requirements.txt --upgrade
