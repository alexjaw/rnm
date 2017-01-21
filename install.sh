#!/usr/bin/env bash
echo Installs and starts the web server...
echo     Works with eth0 and wlan0 if wpa is configured
echo     Does not start access point
echo     Does not install or start any service
echo

WEB_SERVER=rnm/web_server.py
SCRIPTS=scripts

#sh $SCRIPTS/access_point.sh
sh $SCRIPTS/install_pip.sh

echo installing requirements...
sudo pip install -r requirements.txt

echo starting web server...
python $WEB_SERVER
