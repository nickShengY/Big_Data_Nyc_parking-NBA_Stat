#!/bin/sh
../../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /running/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /running/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /running/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../data.csv /running/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input /running/input/* -output /running/output/
/usr/local/hadoop/bin/hdfs dfs -cat /running/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /running/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /running/output/
../../../../stop.sh

