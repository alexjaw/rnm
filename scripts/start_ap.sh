#!/usr/bin/env bash
# Problems with ap startup
# see http://unix.stackexchange.com/questions/119209/hostapd-will-not-start-via-service-but-will-start-directly
# This will start some services but fail on other
sudo service hostapd start

# This will bring up the ap
sudo hostapd /etc/hostapd/hostapd.conf

# This will give us ip
# but the address of the pi itself is weird
# Example 169.254.101.132
sudo service udhcpd start