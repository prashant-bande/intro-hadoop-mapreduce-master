#!C:\Python27\python.exe

import sys

maxHits = 0
contHits = 0
maxPath = None
oldPath = None

# q3: most popular

for line in sys.stdin:
    thisPath = line.strip().split()
    if len(thisPath) != 1:
        continue

    if oldPath and oldPath != thisPath:
        if maxHits < contHits: 
            maxHits = contHits
            maxPath = oldPath

        contHits = 0

    oldPath = thisPath
    contHits += 1

if maxPath != None:
    print maxPath, "\t", maxHits

