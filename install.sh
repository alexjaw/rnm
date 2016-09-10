#!/usr/bin/env bash
echo Installs and starts the web server...
echo     Only works with eth0
echo     Does not start access point
echo     Does not install or start any service
echo

WEB_SERVER=flasky/hello.py
SCRIPTS=scripts

sh $SCRIPTS/access_point.sh
sh $SCRIPTS/install_pip.sh

echo installing requirements...
sudo pip install -r requirements.txt

echo start web server
python $WEB_SERVER
