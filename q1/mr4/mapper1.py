#!/usr/bin/python
import sys
import csv
for line in csv.reader(iter(sys.stdin.readline, '')):
    color = line[33]
# Emit the color and 1 as the key-value pair
    if color:
        print ("{0}\t{1}".format(color,1))
   
