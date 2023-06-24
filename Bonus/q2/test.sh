#!/bin/sh


centroids=("34930 11110 12345" "35170 13610 10910" "35290 11710 10810" "34810 14510 15710" "34890 10810 44990" "34790 40812 14510" "35230 14190 11107")

../../../../start.sh

/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave

/usr/local/hadoop/bin/hadoop dfs -rm -r /task2
/usr/local/hadoop/bin/hadoop dfs -mkdir /task2
/usr/local/hadoop/bin/hadoop dfs -copyFromLocal ../../q1/data.csv /task2

for iter in {0..100};
do



	/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave
	echo "iteration number : $iter "
	echo " input centroids : ${centroids[*]} "



	/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
		-file ./mapper.py -mapper ./"mapper.py \"${centroids[0]}\" \"${centroids[1]}\" \"${centroids[2]}\" \"${centroids[3]}\" \"${centroids[4]}\" \"${centroids[5]}\" \"${centroids[6]}\"" \
		-file ./reducer.py -reducer ./reducer.py \
		-input /task2/data.csv \
		-output /task2/output2


	/usr/local/hadoop/bin/hadoop dfs -cat /task2/output2/part-00000 > test.txt

	flag="False"
	i=0

	while IFS= read -r line;
	do
		if [ "${centroids[$i]}" != "$line" ];
		then
			flag="True"
			echo "mismatch found at $i"
			echo "breaking out of loop to update centroids"
			break
		fi

		i=$((i+1))

	done < test.txt

	if [ "$flag" = "False" ];
	then
		# match was found
		echo "congrats! match was found"
		echo "breaking out of the FOR loop "
		echo " new final centroids are : ${centroids[*]}"
		break

	else

		k=0
		while IFS= read -r line;
		do

			echo "updating centroid at $k"
			centroids[$k]="$line"
			k=$((k+1))


		done < test.txt

		echo " new centroids : ${centroids[*]} "

	fi

	/usr/local/hadoop/bin/hadoop dfs -rm -r /task2/output2


done


# now let's begin with the classification
# our final centroids will still be in the centroids variable


/usr/local/hadoop/bin/hadoop dfs -rm -r /task2
/usr/local/hadoop/bin/hadoop dfs -mkdir /task2
/usr/local/hadoop/bin/hadoop dfs -put ../../q1/data.csv /task2
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave

# starting the second map reduce phase


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
	-file ./mapper2.py -mapper ./"mapper2.py \"${centroids[0]}\" \"${centroids[1]}\" \"${centroids[2]}\" \"${centroids[3]}\" \"${centroids[4]}\" \"${centroids[5]}\" \"${centroids[6]}\"" \
	-file ./reducer2.py -reducer ./reducer2.py \
	-input /task2/data.csv \
	-output /task2/output3


# now print the final output on terminal

/usr/local/hadoop/bin/hadoop dfs -cat /task2/output3/part-00000

# now clean the hdfs file system

/usr/local/hadoop/bin/hadoop dfs -rm -r /task2


../../../../stop.sh










