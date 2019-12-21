#!C:\Python27\python.exe

import sys

active_hours = [0] * 24
last_author_id = None

def print_key_value(author_id, active_hours):
    most_active_hour_count = max(active_hours)
    for hour, count in enumerate(active_hours):
        if count == most_active_hour_count:
            print "{0}\t{1}".format(author_id, hour)

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    author_id, hour = data

    if last_author_id and last_author_id != author_id:
        print_key_value(last_author_id, active_hours)
        active_hours = [0] * 24
        
    last_author_id = author_id
    active_hours[int(hour)] += 1

if last_author_id != None:
    print_key_value(last_author_id, active_hours)

