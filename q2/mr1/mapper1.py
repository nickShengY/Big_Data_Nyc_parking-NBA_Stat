#!/usr/bin/python

import sys
import csv

for line in csv.reader(iter(sys.stdin.readline, '')):
    shooter, defender, result = line[19], line[14], line[13]
    print ("{0}|{1}\t{2}".format(shooter, defender, result))


