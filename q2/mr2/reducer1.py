#!/usr/bin/python
#Input: Key-value pairs from mapper1

import sys

#Initialize the variables
curr_info = None
curr_made = 0
curr_atmp = 0
curr_hit = 0.0


#Read each line of the input
for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    info, made, atmp = data
    Zone = None
    #Check if the current player is the same as the previous one
    if curr_info and curr_info != info:
        #If not, emit the data
        print("{0}\t{1}\t{2}\t{3}".format(curr_info, curr_made, curr_atmp, curr_hit))
        curr_info = None
        curr_made = 0
        curr_atmp = 0
        curr_hit = 0.0
        zone = None
    #Update the current player
    curr_info = info
    
    #Accumulate the shot distance, close defense distance, and shot clock



    curr_made += float(made)
    curr_atmp += float(atmp)
    curr_hit = curr_made/curr_atmp

#Emit the data for the last player
print("{0}\t{1}\t{2}\t{3}".format(curr_info, curr_made, curr_atmp, curr_hit))


