#!C:\Python27\python.exe

import sys

salesCount = 0
salesTotal = 0

# q3: total sales

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    salesTotal += float(thisSale)
    salesCount += 1


print "Total\t", salesTotal
print "Count\t", salesCount

