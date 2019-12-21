#!C:\Python27\python.exe

import sys
import csv
import string

for line in sys.stdin:
    reader = csv.reader(sys.stdin, delimiter='\t')
    
    specials = ',.!?:;"()<>[]#$=-/'
    trans = string.maketrans(specials, ' '*len(specials))
    
    for line in reader:
        if len(line) == 19:
            body = line[4]
            node_id = line[0]
            
            body = body.translate(trans)
            words = body.strip().split()
            
            for word in words:
                print word.lower(), "\t", node_id

