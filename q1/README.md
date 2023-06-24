# Project1-Question 1-NYC Parking Violations Analysis
# Introduction 
***This Directory needs to be placed at "/mapreduce-test/mapreduce-test-python/", failing placing it at the right place could cause the program to crash.***  
  
MapReduce is a programming model based on the idea of dividing a large computational problem into smaller sub-problems that can be processed separately in parallel. The framework consists of two main components: a map phase and a reduce phase. The input data is first split into a set of key-value pairs in the mapper, then passes these pairs to the reducer phase, aggregating them to produce a set of output values. In some complicated cases, it also allows running multiple rounds of MapReduce to get the desired results. It allows multiple machines to handle the tasks in a cluster, making it possible to analyze large datasets efficiently. This project aims to solve two data analysis problems using Hadoop MapReduce-based program. For the first part, we concentrated on the New York City (NYC) Parking Violations data to identify the most common time and location tickets issued, the most usual years and types of cars being ticketed, and the color of cars that get parking tickets the most frequently. To do this, we developed our own Python implementation of the MapReduce framework to analyze the data. Our implementation followed one or multiple rounds of the MapReduce approach. 

# Dataset Description.  
**This data set must place at dir: "/proj1/q1", and the file name of this csv file must be "data.csv"!**

The dataset on NYC Parking Violations is collected by the NYC Department of Finance every year. It is hosted and publicly accessible on the platform known as NYC Open Data, which attempts to give open access to a variety of datasets and data resources published and managed by New York City government organizations. The NYC Parking Violation dataset contains the information on each ticket violation record in New York City. The dataset contains a total of 11535314 rows representing each ticket and 43 columns with more detailed information, such as the date, location the violation occurred, and much more, including the information of vehicles, such as the type and the color of vehicles. 

# MapReduce    
In the first part, we were expected to set up the Hadoop Mapreduce-based framework along with the scheduler for resource management to analyze the violation tickets situation in New York City. We used the NYC Parking Violations 2023 dataset. We analyzed the ticket violations situation during the period of 6/10/2022 to 2/23/2023. Specifically, we were going to answer the following four questions: 
### MapReduce 1:  
When are tickets most likely to be issued?

For this question, we developed a single round of MapReduce.  The purpose of our MapReduce script was to extract the time values from the input dataset, round them down to the nearest hour, and output the resulting hours along with a count of 1 for each hour. This output could then be used as input to a MapReduce job to produce a count of events per hour. 
From our result, the most often time of tickets get issued was 9:00 AM with 999544 counts.   
### Usage    
The mapReduce functions are placed at proj1/q1/mr1, so cd to it first(make sure you have the data at the right place!).      
In the dir, simply bash the test.sh file to run the program.  
### MapReduce 2:  
What are the most common years and types of cars to be ticketed?

For this question, we developed a two-round of MapReduce. In the first Mapreduce we extracted the value of years and types from input data and then produced a year and made, along with 1 a key-value pair at mapper phase. Then passed to the reducer and printed out the aggregated counts of each car year-type pair as our first round of MapReduce outputs. The second MapReduce program chose the year and type of cars with the highest frequency and emitted it as a key-value pair along with the count for each group of key-value pairs with the exact count. Our program showed that the most common years and types of cars to be ticketed was 2021, SUBN, with counts 574105.

### Usage    
The mapReduce functions are placed at proj1/q1/mr2, so cd to it first(make sure you have the data at the right place!).      
In the dir, simply bash the test.sh file to run the program.    
### MapReduce 3:    
Where are tickets most commonly issued?    

For this question, we developed two rounds of MapReduce. From first MapReduce program we got the aggregated counts for each street and location for this station, as the key-value pairs of a combination of street code and location as keys, counts as values. The second MapReduce aggregated the counts and printed the final counts for each location. Our outputs showed that the 3rd Ave, street code 0019, was the ticket most commonly issued place, with counts 31607.   
### Usage  

The mapReduce functions are placed at proj1/q1/mr3, so cd to it first(make sure you have the data at the right place!).      
In the dir, simply bash the test.sh file to run the program.  
### MapReduce 4:    
Which color of the vehicle is most likely to get a ticket?

For this question, we deveoped three rounds of Mapreduce. We used the first round of MapReduce that generated the key-value pairs of color and counts, and then got the aggregated counts for each color at the reducer phase, and followed by the second round of MapReduce to make the counts could be sorted by producing new key-value pairs. After this, we used another round of MapReduce to group the same color together. As a result, we found that WHITE vehicles, with 2781715 times, were the most likely to be ticketed.   
### Usage  

The mapReduce functions are placed at proj1/q1/mr4, so cd to it first(make sure you have the data at the right place!).      
In the dir, simply bash the test.sh file to run the program.  

