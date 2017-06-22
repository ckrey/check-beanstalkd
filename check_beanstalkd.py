#!/usr/bin/env python
# -*- coding: utf-8 -*-

import beanstalkc
import sys
import getopt

def usage():
    print "check-beanstalkd.py"
    print "\t[-h hostname/address]   // default localhost"
    print "\t[-p port]               // default 11300"
    print "\t[-w warning-threshold]  // default 8"
    print "\t[-c critical-threshold] // default 10"
    print "\t[-t tubename]           // default None"
    print "\t[-s stats entry]        // default current-jobs-ready" 
    sys.exit(3)

def main(argv):
    global returnValue
    host = 'localhost'
    port = 11300
    tube = None
    warning = 8
    critical = 10
    stat = 'current-jobs-ready'

    try:
        opts, args = getopt.getopt(argv, "h:p:t:w:c:s:")
    except getopt.GetoptError as e:
        usage();
        print "UNKNOWN"
        sys.exit(3)

    for opt, arg in opts:
        if opt in ('-h'):
            host = arg
        if opt in ('-p'):
            port = int(arg)
        if opt in ('-s'):
            stat = arg
        if opt in ('-t'):
            tube = arg
        if opt in ('-w'):
            warning = int(arg)
        if opt in ('-c'):
            critical = int(arg)

    try:
        beanstalk = beanstalkc.Connection(host=host, port=port)

        if tube == None:
            #pprint(beanstalk.stats())
            s = beanstalk.stats()
            v = s[stat]
            if v < warning:
                print('OK beanstalkd | %s=%d' % (stat, v))
                returnValue = 0
            elif v < critical:
                print('WARNING beanstalkd | %s=%d' % (stat, v))
                returnValue = 1
            else:
                print('CRITICAL beanstalkd | %s=%d' % (stat, v))
                returnValue = 2

        else:
            #pprint(beanstalk.stats_tube(tube))
            s = beanstalk.stats_tube(tube)
            v = s[stat]
            if v < warning:
                print('OK tube %s | s%=%d' % (tube, stat, v))
                returnValue = 0
            elif v < critical:
                print('WARNING tube %s | s%=%d' % (tube, stat, v))
                returnValue = 1
            else:
                print('CRITICAL tube %s | s%=%d' % (tube, stat, v))
                returnValue = 2
            returnValue = 0

    except:
        print('UNKNOWN')

    exit(returnValue)

returnValue = 3

if __name__ == '__main__':
    main(sys.argv[1:])
