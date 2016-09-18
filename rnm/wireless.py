#!/usr/bin/python
#
# Class for interface

import logging
from subprocess import check_output, Popen, PIPE

from interface import Interface

class WiFi(Interface):
    setup_script = '/home/pi/rnm/scripts/setup_wifi.sh'

    def __init__(self):
        Interface.__init__(self, iface='wlan0')  # in python3 only super.__init__()

    def setup(self):
        p = Popen(['sh', self.setup_script], stdout=PIPE, stderr=PIPE)
        return p.communicate()[0]


def test_me():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('------------- Starting test... -------------')

    wifi = WiFi()

    resp = wifi.get_ip()
    logger.info(repr(resp))

    logger.info('-------------    Finished      -------------')

if __name__ == '__main__':
    test_me()