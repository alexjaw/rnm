#!/usr/bin/python
#
# Class for interface and wifi

import logging
from subprocess import check_output, Popen, PIPE

class Interface:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__ + '.Interface')
        # todo: Sometimes we want to run at debug level, how to set that for an
        #       individual class? I get a FileHandler from web_server.py
        #       Right now I do this by setting handler.setLevel(logging.DEBUG)
        #       in web_server.py
        self.logger.info('------------- Starting... -------------')

    def connect(self):
        pass

    def disconnect(self):
        pass


    def get_iface(self):
        # todo: check out this package https://pypi.python.org/pypi/netifaces
        return False

    def get_ip(self):
        ips = check_output(['hostname', '--all-ip-addresses'])
        self.logger.debug('ips = {}'.format(repr(ips)))
        return ips.strip().split()

    def setup(self):
        pass


class WiFi(Interface):
    setup_script = '/home/pi/rnm/scripts/setup_wifi.sh'

    def __init__(self):
        Interface.__init__(self)  # in python3 only super.__init__()

    def setup(self):
        p = Popen(['sh', self.setup_script], stdout=PIPE, stderr=PIPE)
        return p.communicate()[0]

