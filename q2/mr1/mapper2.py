#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        shooter, defender, fear_score = data[0].split("|")[0], data[0].split("|")[1], float(data[1])
        print ("{0}\t{1}|{2}|{3}".format(shooter, defender, fear_score, 1))


