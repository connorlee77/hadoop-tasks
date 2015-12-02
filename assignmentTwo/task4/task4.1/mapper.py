#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET

for line in sys.stdin:  # input from standard input
    root = ET.fromstring(line.strip())
    attrs = root.attrib
    fID, fVAL = '', ''
    try:
        fID = attrs['id'] if 'id' in attrs else attrs['Id']
        fVAL = attrs['posttypeid'] if 'posttypeid' in attrs else attrs['PostTypeId']
    except KeyError:
        continue    
    if fVAL == '1':
        fView = attrs['viewcount'] if 'viewcount' in attrs else attrs['ViewCount']
        print("{0}\t{1}".format(fID, fView))
