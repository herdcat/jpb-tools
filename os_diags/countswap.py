#! /usr/bin/python
import os, re

for PID in os.listdir('/proc'):
  if re.match(r'[0-9]',PID):
    sCount=0
    pName=""
    pFile = open("/proc/%s/smaps" % (PID),'r')
    cFile = open("/proc/%s/status"% (PID),'r')
    for line in pFile.readlines():
      if "swap" in line.lower():
        sCount += int(line.split()[1])
    pName=re.split(r'[\s]',cFile.readlines()[0].strip('\n'))[-1]
    pFile.close()
    cFile.close()
    print "%s: %s" % (pName,sCount)
