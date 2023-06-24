# Question 2-NBA Shot Logs Analysis
# Introduction    
***This Directory needs to be placed at "/mapreduce-test/mapreduce-test-python/", failing placing it at the right place could cause the program to crash.***  
 
MapReduce is a programming model based on the idea of dividing a large computational problem into smaller sub-problems that can be processed separately in parallel. The framework consists of two main components: a map phase and a reduce phase. The input data is first split into a set of key-value pairs in the mapper, then passes these pairs to the reducer phase, aggregating them to produce a set of output values. In some complicated cases, it also allows running multiple rounds of MapReduce to get the desired results. It allows multiple machines to handle the tasks in a cluster, making it possible to analyze large datasets efficiently. This project aims to solve two data analysis problems using Hadoop MapReduce-based program. The second part involved analyzing the NBA shots taken during the 2014-2015 seasons. We aimed to determine each player's "most unwanted defender" based on the fear score. Additionally, we aimed to classify each player's records into four comfortable zones and then considered which zone was the best for James Harden, Chris Paul, Stephen Curry, and LeBron James with the hit rate. To do this, we developed our own Python implementation of the MapReduce framework to analyze the data. Our implementation followed one or multiple rounds of the MapReduce approach. 

# DataSet Description

**This data set must place at dir: "/mapreduce-test/mapreduce-test-python/proj1/q2", and the file name of this csv file must be "shot\_logs.csv"!**

The dataset on NBA Shot Logs records the shots taken during the 2014-2015 season, which provides a rich source of data on the shot-taking behaviour of NBA players. The dataset includes 128069 rows that represent each shot attempts taken by each player throughout the season, and 21 columns show information on who took the shots, who was the nearest defender, time on the shot clock, and much more. 

# MapReduce

In the second part, our purpose was to analyze the NBA Shot Logs dataset during the 2014-2015 season. We were expected to answer the following two questions:
For each pair of the players (A, B), we define the fear sore of A when facing B is the hitrate, such that B is closet defender when A is shoting. Based on the fear sore, for each player, please find out who is his ”most unwanted defender”;
Please develop a MapReduce-based algorithm to classify each player’s records into 4 comfortable zones. Considering the hit rate, which zone is the best for James Harden, Chris Paul, Stephen Curry and Lebron James.

### MapReduce 1
To identify the player's "most unwanted defender" for each player, we designed a two-round Mapreduce. Each round of MapReduce plays a different role in solving this question. We used the first MapReduce to determine the fear score for each shooter/defender pair, which was the shooting result when the shooter faced the defender. The second MapReduce we designed to find out the player's most "unwanted defender", for each player based on the fear score we calculated manually from the first phase.   
### Usage  

The mapReduce functions are placed at proj1/q2/mr1, so cd to it first(make sure you have the data at the right place!).      
In the dir, simply bash the test.sh file to run the program.  
  
### MapReduce 2  
For the second question, we need to classify the shooting player's comfortable zones with the criteria: {SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}. We built the classifier as Zone1: Close shot and got contested in regular time:(shot with 5 feet, the defender is in 3 feet, and the shot clock is in regular time); Zone2: Shots beyond 5 feet and got contested in regular time: (shot over 5 feet, the defender is in 3 feet and the shot clock is in regular time); Zone3: wide-open shots in regular time: (shot from anywhere open, the defender is farther than 3 feet and the shot clock is in regular time); zone4 is otherwise, which means that it is in clutch time:(shoot from anywhere no matter if any defender is contesting). In our first mapper function, we divide the metrics(matrix) into four zones and output each player's shots with a key-value pair with (zone number, made?, 1). Then the stream will push to the reducer1, and the reducer will calculate the hit rate and aggregate each player's every zone along with their hit rates(output:(info, made, attempt, hit rate). In the second mapper, we did not make anything unique, and in reducer2, we found the largest hit rate of their zones for each player. Then we would output the zones with their highest hit rate for each player.

### Usage

The mapReduce functions are placed at proj1/q2/mr2, so cd to it first(make sure you have the data at the right place!).    
In the dir, simply bash the test.sh file to run the program.
