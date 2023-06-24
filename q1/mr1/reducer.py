#!/usr/bin/python

import sys

current_time = None
violations_count = 0

for line in sys.stdin:
    time, count = line.strip().split('\t')
    count = int(count)
    if current_time != time:
        if current_time:
            print("{0}\t{1}".format(current_time, violations_count))
        current_time = time
        violations_count = 0

    violations_count += count

if current_time:
    print("{0}\t{1}".format(current_time, violations_count))


