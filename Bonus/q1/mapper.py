#!/usr/bin/python3

import sys
import csv

header_row = next(csv.reader(sys.stdin))

for line in csv.reader(iter(sys.stdin.readline, '')):
    if line[33] in ["Black", "BLK", "BK", "BK.", "BLAC", "BK/","BCK","BLK.","B LAC","BC"]:
        color = "black"
    
    else:
        color = "not_black"

    if line[9] in ["34510", "10030", "34050"] or line[10] in ["34510", "10030", "34050"] or line[11] in ["34510", "10030", "34050"]:

        print(color+"\t"+"1")


