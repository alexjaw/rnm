#!/usr/bin/python
#
# Class for interface

import logging
from subprocess import check_output, Popen, PIPE, STDOUT

class Interface:
    # todo: check out this package https://pypi.python.org/pypi/netifaces

    def __init__(self, iface, logger=None):
        self.logger = logger or logging.getLogger(__name__ + '.Interface')
        # todo: Sometimes we want to run at debug level, how to set that for an
        #       individual class? I get a FileHandler from web_server.py
        #       Right now I do this by setting handler.setLevel(logging.DEBUG)
        #       in web_server.py
        self.logger.info('------------- Starting... -------------')
        self.iface = iface

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_ip(self):
        # OBS: several os commands have to be use '' and NOT ""
        cmd = ['ip', 'addr', 'show', 'eth0']
        self.logger.debug('os cmd: {}'.format(cmd))
        try:
            iface_info = check_output(cmd).split()
        except OSError as e:
            self.logger.error('Failed with check_output: %s', e.args)
            ip = 'error'
        else:
            inet = iface_info[iface_info.index('inet') + 1]
            ip = inet.split('/')[0]
        self.logger.debug('ip = {}'.format(repr(ip)))
        return ip

    def setup(self):
        pass



def test_me():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info('------------- Starting test... -------------')

    eth = Interface(iface='eth0')

    resp = eth.get_ip()
    logger.info(repr(resp))

    logger.info('-------------    Finished      -------------')

if __name__ == '__main__':
    test_me()
