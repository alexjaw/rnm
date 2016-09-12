#!/usr/bin/env bash
# Will setup environment for a free access point
# file: setup_access_point.sh
conf_files='/home/pi/rnm/scripts'

echo installing config files from $conf_files ...
cd $conf_files
sudo cp interfaces_ap /etc/network/interfaces
sudo cp hostapd_free.conf /etc/hostapd/hostapd.conf
sudo cp hostapd /etc/default/hostapd
echo finished
