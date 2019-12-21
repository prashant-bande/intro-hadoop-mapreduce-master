#!C:\Python27\python.exe

import sys

last_question = None
last_question_length = 0
sum_answers_length = 0
answers_count = 0
average_answers_length = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3:
        continue
    node_id, node_type, body_length = data

    if last_question and last_question != node_id:
        if answers_count > 0:
            average_answers_length = float(sum_answers_length) / float(answers_count)
        print "{0}\t{1}\t{2}".format(last_question, last_question_length, average_answers_length)

        last_question_length = 0
        sum_answers_length = 0
        answers_count = 0
        average_answers_length = 0

    if node_type == 'question':
        last_question_length = int(body_length)
    if node_type == 'answer':
        sum_answers_length += int(body_length)
        answers_count += 1

    last_question = node_id

if last_question is not None:
    if answers_count > 0:
        average_answers_length = float(sum_answers_length) / float(answers_count)
    print "{0}\t{1}\t{2}".format(last_question, last_question_length, average_answers_length)

