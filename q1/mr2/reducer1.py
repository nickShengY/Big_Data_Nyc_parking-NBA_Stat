#!/usr/bin/python

import sys

current_info = None
violations_count = 0

for line in sys.stdin:
    info, count = line.strip().split('\t')
    count = int(count)
    if current_info != info:
        if current_info:
            print ("{0}\t{1}".format(current_info, violations_count))
        current_info = info
        violations_count = 0

    violations_count += count

if current_info:
    print ("{0}\t{1}".format(current_info, violations_count))


