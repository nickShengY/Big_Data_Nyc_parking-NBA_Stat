#!/usr/bin/python
import sys

for line in sys.stdin:
    color, count = line.strip().split('\t')
    try:
        count = int(count)
    except:
        continue
    print("{0}\t{1}".format(count,color))
