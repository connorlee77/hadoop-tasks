#!/usr/bin/python 

import sys

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

def extractRequest(request):
    return request.strip().split()

for line in sys.stdin:
    extract = extractLine(line)
    if extract is not None:
        fileAccessed = ''
        try:
            fileAccessed = extractRequest(extract[2])[1].strip()
        except IndexError:
            continue
        print("{0}".format(fileAccessed))
    else:
        continue
