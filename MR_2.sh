hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file /home/hdfs/vra/Mapper_1.py -mapper /home/hdfs/vra/Mapper_1.py \
-file /home/hdfs/vra/Reducer_1.py -reducer /home/hdfs/vra/Reducer_1.py \
-input /home/hdfs/vra/input/data.csv -output output/all_accidents