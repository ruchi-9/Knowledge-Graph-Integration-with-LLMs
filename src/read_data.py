import psycopg2
from pyspark.sql import SparkSession
import constants

spark = SparkSession.builder.getOrCreate()
conn = psycopg2.connect(
    host=constants.POSTGRESQL_HOST,
    database=constants.POSTGRESQL_DBNAME,
    user=constants.POSTGRESQL_USER, 
    password=constants.POSTGRESQL_PASSWORD,
    port=constants.POSTGRESQL_PORT)

    # SQL query to fetch data
query = "SELECT * FROM titanic1"
cursor = conn.cursor()
cursor.execute(query)
    # Fetch all rows
rows = cursor.fetchall()
cursor.close()
conn.close()
    # Convert fetched data to RDD
    #rdd = spark.sparkContext.parallelize(data_from_postgresql)
    # Create DataFrame from RDD
df = spark.createDataFrame(rows)
df.show()
spark.stop()
