#!/usr/bin/env bash
# Will setup environment for dhcp
# file: setup_dhcp.sh
conf_files='/home/pi/rnm/scripts'

echo installing config files from $conf_files ...
cd $conf_files
sudo cp udhcpd.conf /etc/udhcpd.conf
sudo cp udhcpd_enable /etc/default/udhcpd
sudo cp interfaces_ap /etc/network/interfaces
echo finished