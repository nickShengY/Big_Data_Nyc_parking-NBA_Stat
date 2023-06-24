#!/usr/bin/python

import sys
import csv

for line in csv.reader(iter(sys.stdin.readline, '')):
    year = line[35]
    make = line[6]
    if year and make and year[0] != 'V' and ',1' not in year and int(year)>1500 and int(year)<2024:
        print ("{0},{1}\t{2}".format(year, make,1))

