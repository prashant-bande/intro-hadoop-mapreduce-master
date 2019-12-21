#!C:\Python27\python.exe

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) == 19:
        tagnames = line[2].split()

        for tag in tagnames:
            print tag

