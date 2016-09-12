#!/usr/bin/env bash
# Will setup environment for wifi connection
# file: setup_wifi.sh
conf_files='/home/pi/rnm/scripts'

echo installing config files from $conf_files ...
cd $conf_files
sudo cp interfaces_wifi /etc/network/interfaces
echo finished
