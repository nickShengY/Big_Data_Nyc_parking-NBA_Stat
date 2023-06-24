#!/usr/bin/python
#Input: Key-value pairs from reducer1

import sys

#Read each line of the input
for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    info, made, atmp, hit_rate = data
    print("{0}\t{1}\t{2}\t{3}".format(hit_rate, made, atmp, info))

