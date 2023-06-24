#!/usr/bin/python
#Input: NBA Shot Logs data

import sys
import csv
#Read each line of the input
for data in csv.reader(iter(sys.stdin.readline, '')):

    
    #Extract the shot distance, close defense distance, and shot clock
    if data[19] and data[11] and data[11][0] != 'S' and data[16] and data[16][0] != 'C' and data[8] and data[8][0] != 'S' and data[17] and data[17][0] != 'F':
        shot_dist = float(data[11])
        close_def_dist = float(data[16])
        shot_made = float(data[17])
        shot_clock = float(data[8])
        if shot_dist <= 5 and close_def_dist <= 3 and shot_clock >= 5:
            zone = "Zone 1" #In the paint and contested in regular time
        elif shot_dist > 5 and close_def_dist <= 3 and shot_clock >= 5:
            zone = "Zone 2" #Outside the paint and contested in regular time
        elif close_def_dist > 3 and shot_clock >= 5:
            zone = "Zone 3" #open shot 
        else:
            zone = "Zone 4"
        #Emit the data as key-value pairs
        print("{0}\t{1}\t{2}".format((data[19],zone), shot_made, 1))


