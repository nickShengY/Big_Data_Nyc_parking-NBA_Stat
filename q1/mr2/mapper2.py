#!/usr/bin/python

import sys

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    this_key, this_count = data_mapped
    print ("{0}\t{1}".format(int(this_count),this_key))

