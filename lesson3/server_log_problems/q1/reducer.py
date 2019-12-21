#!C:\Python27\python.exe

# q1: hits to page

import sys

hitsTotal = 0
oldPath = None

# q1: hits to page

for line in sys.stdin:
    thisPath = line.strip().split()
    if len(thisPath) != 1:
        continue

    if oldPath and oldPath != thisPath:
        print oldPath, "\t", hitsTotal
        hitsTotal = 0

    oldPath = thisPath
    hitsTotal += 1

if oldPath != None:
    print oldPath, "\t", hitsTotal

