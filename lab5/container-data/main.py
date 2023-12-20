import json
from datetime import datetime
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('Spark_lab5').config("spark.some.config.option").getOrCreate()
sc=spark.sparkContext
data_file="rides.txt"
rdd=sc.textFile(data_file, minPartitions=100).map(lambda x: eval(x))

time_period=rdd.map(lambda x: (datetime.strptime(x['start_datetime'],"%Y-%m-%d %H:%M:%S").hour,1)).\
            reduceByKey(lambda a,b: a+b).\
            takeOrdered(1,key=lambda trip:-trip[1])
print(time_period)
with open("time_period.json", "w") as f:
   json.dump(time_period,f,indent=4,sort_keys=True)
