#!/usr/bin/python

from time import sleep

i = 0
try:
    while True:
        with open('/home/pi/rnm/rnm/rnm.log', 'a') as f:
            f.write('Hello from rnm.service\n')
        sleep(5)
        i += 1
        if i > 5:
            break
except KeyboardInterrupt, e:
    pass
print "Stopping..."
