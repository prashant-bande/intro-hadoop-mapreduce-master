#!C:\Python27\python.exe

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) == 19:
        author_id = line[3]
        hour = line[8].split(' ')[1].split(':')[0]
        print "{0}\t{1}".format(author_id, hour)

