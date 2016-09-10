#!/usr/bin/env bash
# sh access_point.sh
conf_files='/home/pi/rnm/scripts'

echo updating...
sudo apt-get update -y

echo installing packages...
sudo apt-get install hostapd udhcpd -y

echo installing config files from $conf_files ...
cd $conf_files
sudo cp udhcpd.conf /etc/udhcpd.conf
sudo cp udhcpd_enable /etc/default/udhcpd
sudo cp interfaces_ap /etc/network/interfaces
sudo cp hostapd_free.conf /etc/hostapd/hostapd.conf
sudo cp hostapd /etc/default/hostapd

#echo setting rpi_ap address: 192.168.42.1
#sudo ifconfig wlan0 192.168.42.1

#echo setting update-rc.d...
#sudo update-rc.d hostapd enable
#sudo update-rc.d udhcpd enable

#sudo service hostapd start
#sudo service udhcpd start
#echo reboot...
#sudo reboot
