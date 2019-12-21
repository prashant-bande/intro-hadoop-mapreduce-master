#!C:\Python27\python.exe

import sys

last_node = None
students = []

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    node_id, student = data

    if last_node and last_node != node_id:
        print "{0}\t{1}".format(last_node, students)
        students = []

    last_node = node_id
    students.append(student)

if last_node is not None:
    print "{0}\t{1}".format(last_node, students)

