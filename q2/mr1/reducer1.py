#!/usr/bin/python

import sys

current_shooter, current_defender = None, None
shooter_count, defender_count, hit_count = 0, 0, 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    shooter, defender, result = data[0].split("|")[0], data[0].split("|")[1], data[1]
    if current_shooter == shooter and current_defender == defender:
        shooter_count += 1
        if result == "made":
            hit_count += 1
    else:
        if current_shooter and current_defender:
            print ("{0}|{1}\t{2}".format(current_shooter, current_defender, float(hit_count)/shooter_count))
        current_shooter, current_defender = shooter, defender
        shooter_count, defender_count, hit_count = 1, 0, 0
        if result == "made":
            hit_count += 1

if current_shooter == shooter and current_defender == defender:
    print ("{0}|{1}\t{2}".format(current_shooter, current_defender, float(hit_count)/shooter_count))


