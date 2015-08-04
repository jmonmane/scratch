'''
Copyright (c) 2014 Chet Hosmer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.
'''

'''
usage: python NTPSource.py

'''

import ntplib
import time

NIST = 'nist1-macon.macon.ga.us'

ntp = ntplib.NTPClient()

ntpResponse = ntp.request(NIST)


print

if (ntpResponse):
    now = time.time()
    diff = now-ntpResponse.tx_time
    print 'Difference        : ',
    print diff,
    print 'seconds'

    print 'Network Delay     : ',
    print ntpResponse.delay

    print 'UTC NIST          :  ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(int(ntpResponse.tx_time)))
    print 'UTC SYSTEM        :  ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(int(now)))

else:
    print 'No Response from Time Service'
    
