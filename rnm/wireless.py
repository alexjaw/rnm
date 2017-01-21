#!/usr/bin/python
#
# Class for interface

import logging
from subprocess import check_output, Popen, PIPE
try:
    from wifi import Cell, Scheme
    is_wifi_module = True
except Exception:
    print 'wifi module seems not to be installed'
    is_wifi_module = False

from interface import Interface

class WiFi(Interface):
    setup_script = '/home/pi/rnm/scripts/setup_wifi.sh'

    def __init__(self):
        Interface.__init__(self, iface='wlan0')  # in python3 only super.__init__()
        self._hotspots = []

    def _get_hotspot_info(self, hotspot):
        info = {}
        info['ssid'] = hotspot.ssid
        info['quality'] = hotspot.quality
        info['encrypted'] = hotspot.encrypted
        return info

    def get_hotspots_info(self):
        info = []
        self.scan()
        for hotspot in self._hotspots:
            info.append(self._get_hotspot_info(hotspot))
        return info

    def scan(self):
        self.logger.debug('Scanning...')
        self._hotspots = Cell.all(self.iface)
        for hotspot in self._hotspots:
            self.logger.debug(repr(hotspot))

    def setup(self):
        p = Popen(['sh', self.setup_script], stdout=PIPE, stderr=PIPE)
        return p.communicate()[0]


def test_me():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info('------------- Starting test... -------------')

    wifi = WiFi()

    resp = wifi.get_ip()
    logger.info(repr(resp))

    resp = wifi.get_hotspots_info()

    logger.info('-------------    Finished      -------------')

if __name__ == '__main__':
    test_me()
