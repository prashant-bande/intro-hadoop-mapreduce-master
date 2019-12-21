#!C:\Python27\python.exe

# q1: hits to page

import sys

hitsTotal = 0
oldIP = None

# q2: hits from IP

for line in sys.stdin:
    thisIP = line.strip().split()
    if len(thisIP) != 1:
        continue

    if oldIP and oldIP != thisIP:
        print oldIP, "\t", hitsTotal
        hitsTotal = 0
        
    oldIP = thisIP
    hitsTotal += 1

if oldIP != None:
    print oldIP, "\t", hitsTotal

