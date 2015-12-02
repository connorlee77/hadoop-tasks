#!/usr/bin/python 

import sys
import datetime
import time

def extractLine(line):
    
    #Check if line exists
    if line is None:
        return

    host = ''
    rest = ''
    #handle error if format is incorrect
    try:
        host, rest = line.strip().split('- -')
    except Exception:
        return 
    
    found = False
    i = 0
    j = len(rest) - 1
    while i < j:
        if rest[i] != '\"':
            i += 1     
        if rest[j] != '\"':
            j -= 1
        if rest[i] == '\"' and rest[j] == '\"':
            break
        if rest[i] == '\"' or rest[j] == '\"':
            found = True
    if not found:
        return    
    timestamp = ''
    request = ''
    reply = ''
    byte = ''
    try:
        timestamp = rest[0 : i - 1].strip()
        request = rest[i + 1 : j].strip()
        replyAndBytes = rest[j + 1: ].strip()
        reply, byte = replyAndBytes.strip().split()
    except Exception:
        return

    return (host.strip(), timestamp.strip(), request.strip(), reply.strip(), byte.strip())


for line in sys.stdin:
    extract = extractLine(line)
    if extract is not None:
        reply = ''
        host = ''
        try:
            host = extract[0].strip()
            timestamp = extract[1].strip()[1:-6].strip()
            dt = datetime.datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S").strftime('%s')
            
        except IndexError:
            continue
        print("{0}\t{1}".format(host, dt))
