# rnm
Raspberry Network Manager (jessie)

Purpose: Provide services that can connect a headless raspberry to a wifi network. Let's say we have a device equipped with a rpi and that we place it in a new wifi environment. Then we would like to have an easy way (for non-technical end-users) to enable wireless networking for our device. If the device does not find a guest network, then it should start an access point and provide some service for further wifi network configuration.

Similar projects:
(search for "wifi" on pypi)
- smartanthill: : http://smartanthill-20.readthedocs.io/en/latest/

Starting points:
- Raspbian jessie networking is using /etc/dhcpcd, previously configured with /etc/network/interfaces, see for example http://raspberrypi.stackexchange.com/questions/39785/dhcpcd-vs-etc-network-interfaces
- Debian network configurations: https://wiki.debian.org/NetworkConfiguration
- Access Point setup: http://elinux.org/RPI-Wireless-Hotspot
- Working with WiFi: https://github.com/rockymeza/wifi
- Working with hostapd.conf: https://pypi.python.org/pypi/pyhostapdconf/1.0
- Network Manager (dbus): http://dev.iachieved.it/iachievedit/exploring-networkmanager-d-bus-systemd-and-raspberry-pi/
- Reading and replacing config values in linux conf files - general methods: http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python?rq=1
- Starting simple service using systemd: http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/ 

Conf files affected:
- /etc/udhcpd.conf
- /etc/default/udhcpd
- /etc/network/interfaces
- /etc/hostapd/hostapd.conf 
- /etc/default/hostapd

Some Debian commands:
- sudo apt-get install hostapd udhcpd -y
- (optional) sudo ifconfig wlan0 [static ip-address]
- sudo service hostapd <action>
- sudo service udhcpd <action>
- sudo update-rc.d hostapd [enable/disable]
- sudo update-rc.d udhcpd [enable/disable]

Experimenting:
- Starting with Jessie light on rpi2
- update and upgrade, https://www.raspberrypi.org/documentation/raspbian/updating.md
- Installation of hostapd and udhcpd
