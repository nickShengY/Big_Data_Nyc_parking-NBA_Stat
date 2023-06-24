#!/usr/bin/python

import sys
import csv

for line in csv.reader(iter(sys.stdin.readline, '')):
    streetname = line[24]
    location = line[13]
    if location:
        print ("{0},{1}\t{2}".format(location,streetname,1))

