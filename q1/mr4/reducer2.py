#!/usr/bin/python

import sys

for line in sys.stdin:
    this_count, this_color = line.strip().split('\t')
    print ("{0}\t{1}".format(this_color, this_count))
