#!/usr/bin/python

import sys

current_shooter = None
max_fear_score, max_defender, count = 2, None, 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    shooter, defender, fear_score, count = data[0], data[1].split("|")[0], float(data[1].split("|")[1]), int(data[1].split("|")[2])
    if current_shooter == shooter:
        if fear_score < max_fear_score and fear_score != 0:
            max_fear_score, max_defender = fear_score, defender
    else:
        if current_shooter:
            print ("{0}\t{1},{2}".format(current_shooter, max_defender, max_fear_score))
        current_shooter = shooter
        max_fear_score, max_defender = fear_score, defender

if current_shooter == shooter:
    print ("{0}\t{1},{2}".format(current_shooter, max_defender, max_fear_score))


