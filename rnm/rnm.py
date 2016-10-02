#!/usr/bin/python

import logging

from service import AccessPoint, DHCP
from wireless import Interface, WiFi

class RaspberryNetworkManager:
    '''...service...'''

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__ + '.RaspberryNetworkManager')
        # todo: Sometimes we want to run at debug level, how to set that for an
        #       individual class? I get a FileHandler from web_server.py
        #       Right now I do this by setting handler.setLevel(logging.DEBUG)
        #       in web_server.py
        self.logger.info('------------- Starting... -------------')
        self.eth = Interface(iface='eth0', logger=logger)
        self.wlan = Interface(iface='wlan0', logger=logger)
        self.wifi = WiFi()

    def get_mode(self):
        ''' Should probably return something saying if its acting as ap
            or if it's connected to lan and/or wifi - definitly not
            just a string'''
        return False

    def scan_wifi(self):
        # scan wifi neigbourhood
        # todo: check out https://github.com/rockymeza/wifi
        return False

    def start_accesspoint(self):
        return False


def test_me():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('------------- Starting test... -------------')

    wifi = WiFi()
    ap = AccessPoint()
    dhcp = DHCP()

    logger.info('-------------    Finished      -------------')

if __name__ == '__main__':
    test_me()
