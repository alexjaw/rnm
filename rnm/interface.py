#!/usr/bin/python
#
# Class for interface

import logging
from subprocess import check_output, Popen, PIPE, STDOUT


class Interface:
    """ Class to create interfaces such as eth0, wlan0, etc...

    :arg str iface: name of the interface, eth0, wlan0, etc...
    :arg Logger: Normally provided in instantiation, but optional

    :ivar string iface: see above
    :ivar Logger logger: for logging

    .. seealso:: Where it is used --
        :py:meth: 'wireless.WiFi'

    .. note:: Similar package https://pypi.python.org/pypi/netifaces
    """

    def __init__(self, iface, logger=None):
        self.iface = iface
        self.logger = logger or logging.getLogger(__name__ + '.Interface')
        # todo: Sometimes we want to run at debug level, how to set that for an
        #       individual class? I get a FileHandler from web_server.py
        #       Right now I do this by setting handler.setLevel(logging.DEBUG)
        #       in web_server.py
        self.logger.info('------------- Starting... -------------')

    def _interface_cmd(self, cmd):
        p = Popen(['sudo', cmd, self.iface], stdout=PIPE, stderr=PIPE)
        # todo: should do with info from p.communicate()
        resp = p.communicate()
        self.logger.debug('stdout: %s', repr(resp[0]))
        self.logger.debug('stderr: %s', repr(resp[1]))
        if p.returncode == 0:
            return True
        else:
            return False

    def connect(self):
        if self._interface_cmd('ifup'):
            self.logger.info('connected')
            return True
        else:
            self.logger.error('connection failed')
            return False

    def disconnect(self):
        if self._interface_cmd('ifdown'):
            self.logger.info('disconnected')
            return True
        else:
            self.logger.error('disconnection failed')
            return False

    def get_ip(self):
        """Get IP for the interface, e.g. ifconfig eth0"""
        # OBS: several os commands have to be use '' and NOT ""
        cmd = ['ip', 'addr', 'show', self.iface]
        self.logger.debug('os cmd: {}'.format(cmd))
        try:
            iface_info = check_output(cmd).split()
        except OSError as e:
            self.logger.error('Failed with check_output: %s', e.args)
            ip = 'error'
        else:
            try:
                inet = iface_info[iface_info.index('inet') + 1]
            except ValueError as e:
                self.logger.debug('ValueError for inet: %s', e.args)
                ip = 'no IP - not connected'
            else:
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
    wlan = Interface(iface='wlan0')

    resp = eth.get_ip()
    logger.info(repr(resp))

    resp = wlan.get_ip()
    logger.info(repr(resp))

    resp = wlan.disconnect()
    # logger.info(repr(resp))

    resp = wlan.connect()
    # logger.info(repr(resp))

    logger.info('-------------    Finished      -------------')


if __name__ == '__main__':
    test_me()
