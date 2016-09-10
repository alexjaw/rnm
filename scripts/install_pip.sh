#!/usr/bin/env bash
# We need pip
# Download to a download folder
DIRECTORY=downloads
GETPIP=get-pip.py

cd ~

echo checking folder....
if [ -d "$DIRECTORY" ]; then
    echo $DIRECTORY foldder exist
else
    echo creating folder $DIRECTORY...
    mkdir $DIRECTORY
fi

echo downloading $GETPIP ...
cd ~/$DIRECTORY
wget https://bootstrap.pypa.io/get-pip.py

echo installing $GETPIP...
sudo python $GETPIP

echo finished.
cd ~