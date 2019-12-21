#!C:\Python27\python.exe

import sys

N = 10
topN_tag = [None] * N
topN_tag_count = [0] * N
last_tag = None
last_tag_count = 0


def get_min():
    count = min(topN_tag_count)
    index = topN_tag_count.index(count)
    return count, index


def update_top(index):
    topN_tag[index] = last_tag
    topN_tag_count[index] = last_tag_count


for line in sys.stdin:
    tag = line.strip()

    if tag:  # if it consists of one value
        if last_tag and last_tag != tag:
            min_count, min_index = get_min()
            if last_tag_count > min_count:
                update_top(min_index)
            last_tag_count = 0

        last_tag = tag
        last_tag_count += 1

if last_tag is not None:
    min_count, min_index = get_min()
    if last_tag_count > min_count:
        update_top(min_index)

    order = sorted(range(N), key=lambda k: topN_tag_count[k], reverse=True)

    for i in range(N):
        print '{0}\t{1}'.format(topN_tag[order[i]], topN_tag_count[order[i]])

