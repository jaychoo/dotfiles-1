#!/bin/bash

# Set up some dropbox links

if [ -d $HOME/Dropbox ]; then
    [ ! -L $HOME/Documents/Calibre ] && ln -s -f $HOME/Dropbox/Calibre $HOME/Documents/Calibre
    [ ! -L $HOME/Documents/iChats ] && ln -s -f $HOME/Dropbox/iChats $HOME/Documents/iChats
    [ ! -L $HOME/Presentations ] && ln -s -f $HOME/Dropbox/Presentations $HOME/Presentations
    [ ! -L $HOME/Shrapnel ] && ln -s -f $HOME/Dropbox/Shrapnel $HOME/Shrapnel
    [ ! -L $HOME/Desktop/Shrapnel ] && ln -s -f $HOME/Dropbox/Shrapnel $HOME/Desktop/Shrapnel
    [ ! -L "$HOME/Library/Application Support/Sublime Text 3" ] && ln -s -f "$HOME/Dropbox/Sublime Text 3" "$HOME/Library/Application Support/Sublime Text 3"
    [ ! -L $HOME/.bash_history ] && ln -s $HOME/Dropbox/history/bash_history $HOME/.bash_history
    [ ! -L $HOME/.psql_history ] && ln -s $HOME/Dropbox/history/psql_history $HOME/.psql_history
fi
