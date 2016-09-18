#!/usr/bin/python
#
# Classes for accesspoint and dhcp services

import logging
from subprocess import check_output, Popen, PIPE

class Service:
    def __init__(self, service):
        self.service = service

    def _service_cmd(self, cmd):
        assert cmd in ['start', 'stop', 'status'], 'Not a valid service cmd'
        p = Popen(['sudo', 'service', self.service, cmd], stdout=PIPE, stderr=PIPE)

        # todo: should do with info from p.communicate()
        resp = p.communicate()[0].split('\n')
        rv = {'LSB': None, 'Loaded': None, 'Active': None}
        for line in resp:
            if '\xe2\x97\x8f' in line:
                rv['LSB'] = line.split(':')[1].strip()
            elif 'Loaded' in line:
                rv['Loaded'] = line.split(':')[1].strip()
            elif 'Active' in line:
                rv['Active'] = line.split(':')[1].strip()
        return rv

    def start(self):
        return self._service_cmd('start')

    def stop(self):
        return self._service_cmd('stop')

    def status(self):
        return self._service_cmd('status')


class AccessPoint(Service):
    setup_script = '/home/pi/rnm/scripts/setup_access_point.sh'

    def __init__(self):
        Service.__init__(self, 'hostapd')

    def setup(self):
        p = Popen(['sh', self.setup_script], stdout=PIPE, stderr=PIPE)
        return p.communicate()[0]


class DHCP(Service):
    setup_script = '/home/pi/rnm/scripts/setup_dhcp.sh'

    def __init__(self):
        Service.__init__(self, 'udhcpd')

    def setup(self):
        p = Popen(['sh', self.setup_script], stdout=PIPE, stderr=PIPE)
        return p.communicate()[0]

