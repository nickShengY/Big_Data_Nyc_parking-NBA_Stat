#!/usr/bin/python3

import sys
import numpy as np
from numpy.linalg import norm
import re


c1 = np.array(sys.argv[1].split()).astype(np.float64)       # any 7 random data points
c2 = np.array(sys.argv[2].split()).astype(np.float64)   
c3 = np.array(sys.argv[3].split()).astype(np.float64)
c4 = np.array(sys.argv[4].split()).astype(np.float64)
c5 = np.array(sys.argv[5].split()).astype(np.float64)
c6 = np.array(sys.argv[6].split()).astype(np.float64)
c7 = np.array(sys.argv[7].split()).astype(np.float64)


pat_st_name = re.compile(r'^W\s[5-7][0-9]')    # to fetch W 57 from street name
pat_st_num = re.compile((r'\d\d'))             # to fetch 57 from street name

centroids = np.array([c1,c2,c3,c4,c5,c6,c7])

cluster_map = dict()

for line in sys.stdin:

    line = line.strip()
    line = line.split(',')

    if line[0] == "Summons Number":         # skip the header row
        continue

    precinct = int(line[14])                # Manhattan North has precinct  = 20 (fetch the 0.5 mile radius)
    street_name = line[24]
    
    try:
        time = line[19]
        time = time.strip()

        if len(time)!=5 and "." in time:                      # must be a 5-character string
            continue

        hours = int(time[0:4])                # example : 1030
        shift = time[4]                       # Am or Pm
    
    except:
        continue


    # Data Filters:
    # Streets taken from W 52 till W 72
    # Precinct = 20 restricts area close to Lincoln Center (0.5 Miles) on those streets
    # time window taken from 9.30 AM till 10.30 AM (assuming car will be parked around 10 AM)

    if shift!="A" or (hours < 930 or hours > 1030):
        continue

    if precinct!= 20:
        continue

    street_name = pat_st_name.findall(street_name)          # ['W 66']
    if street_name:
        street_name = street_name[0]                        # 'W 66'
        street_num = pat_st_num.findall(street_name)        # ['66']
        if not street_num:
            continue
        else:
            street_num = int(street_num[0])                 # 66

    else:
        continue

       

    # Restricting Area under consideration using street numbers
    if street_num > 72 or street_num < 52 :
        continue
    

    # finall we have the data we need!

    sc1 = float(line[9])
    sc2 = float(line[10])
    sc3 = float(line[11])

    if not sc1 or not sc2 or not sc3:
        continue

    datapoint = np.array([sc1,sc2,sc3])

    distance = np.zeros(len(centroids))

    for k in range(len(centroids)):

        row  = norm(datapoint - centroids[k], axis = 0)    
        distance[k] = np.square(row)
    
    nearest_cluster = np.argmin(distance,axis=0)

    if nearest_cluster in cluster_map:
        cluster_map[nearest_cluster].append([datapoint,1])

    else:
        cluster_map[nearest_cluster] = list()
        cluster_map[nearest_cluster].append([datapoint,1])

# combiner


for key, val in cluster_map.items():
    temp = np.zeros(len(val[0][0]))  
    count = 0

    for v in val:
        temp += v[0] 
        count += v[1]
    cluster_map[key] = [temp,count]



for key, val in cluster_map.items():
    zone = str(key)
    f = val[0][0]
    s = val[0][1]
    t = val[0][2]
    c = val[1]
    print(zone+"\t"+str(f)+"_"+str(s)+"_"+str(t)+"_"+str(c))

    # val is a list which contains two things for each centroid(key) : 1. partial sum of all datapoints
                                                                    #  2. count of all datapoints
    # all this output will be sorted before getting to reducer, so can be taken advantage of 
    # take sum of all points from all mappers belonging to one centroid and divide by total count, ---> this will give new centroid of that cluster
    








