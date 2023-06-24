# Bonus Question
***This Directory needs to be placed at "/mapreduce-test/mapreduce-test-python/", failing placing it at the right place could cause the program to crash.***    
K-Means is an unsupervised machine learning algorithm that is commonly used for clustering and segmentation analysis. The algorithm is based on the idea of grouping similar data points into a fixed number of clusters. However, K-Means' biggest challenge is determining the optimal number of classes. This will significantly affect the prediction accuracy of the model. In the Bonus Question, we aimed to develop a MapReduce-based program based on the K-Means algorithm, first to predict the probability of getting a ticket if a black car parking illegally at street codes 34510, 10030, 34050, second to define the parking place that if walking within 0.5 miles to get Lincoln Center. We still worked on the NYC Parking Violations dataset to answer the bonus question.
# DataSet Description:    
Same as Question 1.  
**The data must be placed at "/proj1/q1", and the file name of this csv file must be: "data.csv"** 

# MapReduce

### MapReduce 1:  
We first classified the color of parked vehicles into two categories: either black vehicles or not, and if the parking location matched any of the three specified street codes, then produced a key-value pair of color,1 at the mapper phase. The reducer then aggregated the counts for black or not black separately and calculated the probability of black vehicles parked at the given location receiving a ticket using the count of black vehicles that received a ticket and the total count of black vehicles parked illegally. The probability was predicted as 0.884.
#### Usage: 
The MapReduce function are placed at proj1/Bonus/q1, so cd to it first and make sure you have the data at the right place!   
### MapReduce 2:  
For the second question, we developed two rounds of MapReduce to segment the parking areas into different zones based on their proximity to Lincoln Center and recommend the zone with the most parking spots within the 0.5-mile walking distance. In the frist round of MapReduce, we computed the mean of all data points in the cluster, which was the total sum of all points divided by the total number of points. In the second round of MapReduce, we found the zone with particular datapoints lied so that we knew the zone to which the data point was closest. Then we collected the set of data points that were closest to this zone and whether there was a ticket violation at this point. Now we got the number of parking tickets for each zone from every mapper, and then we printed out the zone with the minimum number of parking tickets as the favourable parking zone, which was zone 2.

#### Usage: 
Install the prerequisite package first with: pip install numpy   

The MapReduce function are placed at proj1/Bonus/q2, so cd to it first and make sure you have the data at the right place!   

