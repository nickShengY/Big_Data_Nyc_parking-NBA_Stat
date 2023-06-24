#!/usr/bin/python

import sys

current_group = None
total_count = 0

for line in sys.stdin:
    group, count = line.strip().split("\t")
    count = int(count)
    if current_group != group:
        if current_group:
            print("{0}\t{1}".format(current_group, total_count))
        current_group = group
        total_count = 0
    total_count += count

if current_group:
    print("{0}\t{1}".format(current_group, total_count))







