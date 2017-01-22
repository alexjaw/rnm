#!/usr/bin/python
import os
import time
from subprocess import check_output, Popen, PIPE
magic_file = 'scan' 
scan_results_outfile = 'scan_results.txt'
homedir = '/home/pi/'
scan_results_file = os.path.join(homedir, scan_results_outfile)

print 'Starting scan of wifi...'
f = os.path.join(homedir, magic_file)
if not os.path.exists(f):
    print 'Exit. Magic file, {}, missing.'.format(f)
    exit(0)

def shell_cmd(cmd):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    if err:
        print err
        return -1
    else:
        #print out
        return out

def is_scanning_possible():
    s_fail = 'Failed to connect to non-global ctrl_ifname'
    resp = shell_cmd(['wpa_cli', 'scan'])
    time.sleep(1)
    if resp == -1:
        return -1
    elif resp == s_fail:
        return False
    else:
        return True

def scan_wifi():
    resp = is_scanning_possible()
    if resp == -1:
        return -1
    elif not resp:
        print 'Scanning not possible'
        return -1
    elif resp:
        print 'Scanning...'
    
    resp = shell_cmd(['wpa_cli', 'scan_results'])
    time.sleep(1)
    if resp == -1:
        return -1
    
    check = check_if_rescan_needed(resp)
    if check:
        return 'rescan'
    return resp

def check_if_rescan_needed(resp):
    data = []
    _ = resp.split('\n')
    for item in _:
        if item != '':
            print item
            data.append(item)
    n = len(data)
    print 'Data entries = {}'.format(n)
    if n < 3:
        print 'Rescanning needed.'
        return True
    return False


resp = scan_wifi()
if resp == -1:
    exit(1)
elif resp == 'rescan':
   resp = scan_wifi()

with open(scan_results_file, 'w') as f:
   f.write(time.strftime("%c") + '\n')
   f.write(resp)
   print 'Scan results saved in {}'.format(scan_results_file)
