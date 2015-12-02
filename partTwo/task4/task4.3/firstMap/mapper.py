#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET

for line in sys.stdin:  # input from standard input
    root = ET.fromstring(line.strip())
    attrs = root.attrib
    fID, fVAL, fView = '', '', ''
    try:
        fID = attrs['Id']
        fVAL = attrs["PostTypeId"]
    except KeyError:
        continue 
    if fVAL == '1':
        try:
            fView = attrs['AcceptedAnswerId']
        except KeyError:
            continue
        print("{0}\t{1}\t{2}".format(fView, fVAL, fID))   
    if fVAL == '2':
        try:
            fView = attrs['OwnerUserId']
        except KeyError:
            continue
        print("{0}\t{1}\t{2}".format(fID, fVAL, fView))
