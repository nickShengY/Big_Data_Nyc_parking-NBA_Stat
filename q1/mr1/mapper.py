#!/usr/bin/python
import sys
import csv

for line in csv.reader(iter(sys.stdin.readline, '')):
    time = line[19]
    if time and time[0] != 'V' and time[0] != '.' and len(time) == 5 and (time[0] == '1' or time[0] == '0'):
        if time[:-3] == '00' and time[4] == 'A':
            hour = time[:-3] + ':00 ' + time[4] + 'M.'
        elif time[:-3] == '00' and time[-1] == 'P':
            hour = time[:-3] + ':00 ' + time[4] + 'M.'
        elif time[0] == '0' or (time[0] == '1' and (time[1] == '0' or time[1] == '1' or time[1] == '2')):
            hour = time[:-3] + ':00 ' + time[4] + 'M.'
            print("{0}\t1".format(hour))


