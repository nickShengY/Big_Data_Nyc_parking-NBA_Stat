#!/bin/sh
../../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /running/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /running/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /running-2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /running-3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /running/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../data.csv /running/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper1.py -mapper mapper1.py \
-file reducer1.py -reducer reducer1.py \
-input /running/input/* -output /running/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-nr \
-file mapper2.py -mapper mapper2.py \
-file reducer2.py -reducer reducer2.py \
-input /running/output/* -output /running-2/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper3.py -mapper mapper3.py \
-file reducer3.py -reducer reducer3.py \
-input /running-2/output/* -output /running-3/output/

/usr/local/hadoop/bin/hdfs dfs -cat /running-3/output/part-00000 | head -10
/usr/local/hadoop/bin/hdfs dfs -rm -r /running/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /running/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /running-2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /running-3/output/

../../../../stop.sh










