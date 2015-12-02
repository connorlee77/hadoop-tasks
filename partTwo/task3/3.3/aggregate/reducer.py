#!/usr/bin/python 

import sys
import datetime


def printTime(lastTime, firstTime, prev):
    
    last = int(lastTime)
    first = int(firstTime)

    tLast = datetime.datetime.fromtimestamp(last)
    tFirst = datetime.datetime.fromtimestamp(first)
    if last != 0:
        print("{0}\t{1}".format(prev, (tLast - tFirst).seconds))
    else:
        print("{0}\t{1}".format(prev, tFirst.strftime("%d/%b/%Y:%H:%M:%S -0400"))) 

firstTime = '0'
prev = ''
lastTime = '0'
for line in sys.stdin:
    host, seconds = line.strip().split()
    
    if host == prev:
        lastTime = seconds
    else:
 
        if prev != '':   
            printTime(lastTime, firstTime, prev)
        
        prev = host
        firstTime = seconds
        lastTime = '0'
      
printTime(lastTime, firstTime, prev)


