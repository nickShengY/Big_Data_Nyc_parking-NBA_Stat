#!/usr/bin/python

import sys

current_count = None
current_key = None
key = None

# input comes from STDIN
for line in sys.stdin:


    this_count, this_key = line.strip().split('\t')

    if current_count == this_count:
        key = this_key
    else:
        if current_count:
            print ("{0}\t{1}".format(key, int(current_count)))
        current_count = this_count
        key = this_key

if current_count == this_count:
    print ("{0}\t{1}".format(key, int(current_count)))




