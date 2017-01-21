#!/usr/bin/python
from subprocess import check_output, Popen, PIPE

def shell_cmd(cmd):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    if err:
        print err
        return -1
    else:
        #print out
        return out

def is_service_running(serv):
    cmd = ['systemctl', 'status', serv,]
    resp = shell_cmd(cmd)
    if resp == -1:
        return -1

    if 'running' in resp:
        return True
    else:
        return False

def service_restart(serv):
    cmd = ['systemctl', 'restart', serv,]
    resp = shell_cmd(cmd)
    if resp == -1:
        return -1
    else:
        return 0

def service_start(serv):
    '''If not running, will try to restart'''
    #serv = 'udhcpd'
    resp = is_service_running(serv)
    print '{} running status: {}'.format(serv, resp)
    if resp:
        return 0
    elif not resp:
        if service_restart(serv) == -1:
            return -1
        else:
            resp = is_service_running(serv)
            print '{} running status: {}'.format(serv, resp)
            if not resp:
                return -1
            elif resp:
                return 0

def ap_address(addr='192.168.42.1'):
    resp = shell_cmd(['hostname', '-I',])
    if resp == -1:
        return -1
    print 'addresses: {}'.format(resp)
    if addr in resp:
        return 0
    else:
        resp = shell_cmd(['ifconfig', 'wlan0', addr,])
    if resp == -1:
        return -1
    else:
        resp = shell_cmd(['hostname', '-I',])
        if resp == -1:
            return -1
        print 'addresses: {}'.format(resp)
        if addr in resp:
            return 0
        else:
            return -1


print 'Testing...'
print ap_address()
serv = 'hostapd'
print service_start(serv)
serv = 'udhcpd'
print service_start(serv)
