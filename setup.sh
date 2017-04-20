#!/usr/bin/env bash

# check if it is MACOSX
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Installing dependencies for the workshop"
else
    echo "This script is only compatible with MACOSX"
    exit 1
fi

# check if brew is installed
which -s brew
if [[ $? != 0 ]] ; then
    # Install Homebrew
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
else
    brew update
fi

# install selenium server and chrome driver
brew install selenium-server-standalone chromedriver carthage ideviceinstaller

# install python3
brew install python3

# install all dependencies
pip install -r requirements.txt

# open python interpreter
bpython
