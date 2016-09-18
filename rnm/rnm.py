#!/usr/bin/python

import logging

from service import AccessPoint, DHCP
from wireless import Interface, WiFi

class RaspberryNetworkManager:
    '''...service...'''

    def __init__(self):
        self.netcon = Interface()

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
