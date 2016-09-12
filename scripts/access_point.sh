#!/usr/bin/env bash
# Installs the dependencies for access point
# sh access_point.sh
conf_files='/home/pi/rnm/scripts'

echo updating...
sudo apt-get update -y

echo installing packages...
sudo apt-get install hostapd udhcpd -y

echo finished