import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Read the CSV file into a DataFrame
df = spark.read.csv('', header=True, inferSchema=True)

# Display the DataFrame
df.show()