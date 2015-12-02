#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET

for line in sys.stdin:  # input from standard input
    root = ET.fromstring(line.strip())
    attrs = root.attrib
    fID, fVAL = '', ''
    try:
        fID = attrs['ParentId']
        fVAL = attrs["PostTypeId"]
        fView = attrs['OwnerUserId']
    except KeyError:
        continue    
    if fVAL == '2':
        print("{0}\t{1}".format(fID, fView))
