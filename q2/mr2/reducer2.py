#!/usr/bin/python
#Input: Key-value pairs from mapper2

import sys




curr_player = None
curr_made = 0
curr_atmp = 0
curr_hit = 0.0
curr_zone = None

#Read each line of the input
for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    hit_rate, made, atmp, info = data
    info = info.split(',')
    player = info[0][2:-1]
    zone = info[1][2:-2]



    
    if curr_player == player:
        if curr_hit < hit_rate:
            curr_hit, curr_zone = hit_rate, zone
    else:
        if curr_player:
            print("{0}\t{1}\t{2}".format(curr_player, curr_zone, curr_hit))
        curr_player = player
        curr_hit, curr_zone = hit_rate, zone


if curr_player == player:
    print("{0}\t{1}\t{2}".format(curr_player, curr_zone, curr_hit))




