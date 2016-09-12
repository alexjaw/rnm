#!/usr/bin/python

from subprocess import check_output, Popen, PIPE
from time import sleep

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


class NetworkConnection:
    def __init__(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass


    def get_iface(self):
        # todo: check out this package https://pypi.python.org/pypi/netifaces
        return False

    def get_ip(self):
        ips = check_output(['hostname', '--all-ip-addresses'])
        return ips.strip().split()

    def setup(self):
        pass


class WiFi(NetworkConnection):
    setup_script = '/home/pi/rnm/scripts/setup_wifi.sh'

    def __init__(self):
        NetworkConnection.__init__(self)

    def setup(self):
        p = Popen(['sh', self.setup_script], stdout=PIPE, stderr=PIPE)
        return p.communicate()[0]


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


class RaspberryNetworkManager:
    '''...service...'''

    def __init__(self):
        self.netcon = NetworkConnection()

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


def to_logfile(log_this):
    with open('/home/pi/rnm/rnm/rnm.log', 'a') as f:
        f.write(repr(log_this))
        f.write('\n')

def temp_test():
    i = 0
    try:
        while True:
            to_logfile('Hello from rnm.service\n')
            sleep(5)
            i += 1
            if i > 5:
                break
    except KeyboardInterrupt, e:
        pass
    print "Stopping..."

def test_me():
    netcon = NetworkConnection()
    wifi = WiFi()
    ap = AccessPoint()
    dhcp = DHCP()

    ips = netcon.get_ip()
    to_logfile(repr(ips))
    assert type(ips) == list

    resp = ap.status()
    to_logfile(resp)

    resp = dhcp.status()
    to_logfile(resp)

    resp = wifi.setup()
    to_logfile(resp)

    to_logfile('---------- finished ----------')

if __name__ == '__main__':
    test_me()
