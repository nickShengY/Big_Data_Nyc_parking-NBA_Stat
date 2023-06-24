#!/usr/bin/python
import sys


color_groups = {
    'BLACK': ['BLK', 'BK', 'BLACK'],
    'BLUE': ['BL', 'BLUE'],
    'BROWN': ['BR', 'BROWN'],
    'GRAY': ['GRY', 'GREY', 'GY'],
    'GREEN': ['GR'],
    'RED': ['RD', 'RED'],
    'WHITE': ['WHI', 'WHITE', 'WH'],
}

for line in sys.stdin:
    line = line.strip()
    color, count = line.split("\t")
    for group in color_groups:
        if color in color_groups[group]:
            print("{0}\t{1}".format(group, count))


