from rdflib import Graph, Literal, Namespace, RDF, URIRef
from pyspark.sql import SparkSession
from io import BytesIO
import constants
from minio import Minio 
import psycopg2


# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Create TTL File") \
    .getOrCreate()
"""
# Sample data
data = [("John 12", 25, "Engineer", "New York"),
        ("Alice", 30, "Manager", "San Francisco"),
        ("Bob", 35, "Doctor", "Los Angeles"),("Bob", 45, "Doctor", "Los Angeles")]
"""
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
#print(df.collect())

# Define namespaces
ex = Namespace("http://example.org/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()

# Define predicates
hasPassengerId = ex.hasPassengerId
hasSurvived = ex.hasSurvived
hasClass = ex.hasClass
hasName = ex.hasName
hasSex= ex.hasSex
hasAge = ex.hasAge
hasSibSp = ex.hasSibSp
hasParch = ex.hasParch
hasTicket = ex.hasTicket
hasFare = ex.hasFare
hasCabin = ex.hasCabin
hasEmbarked = ex.hasEmbarked


# Iterate through the data and add triples to the graph
for row in df.collect():
    subject = ex[row[0].replace(" ", "_")]  # Assuming names are unique identifiers
    g.add((subject, RDF.type, ex.hasPassengerId))
    g.add((subject, hasSurvived, Literal(row[0], datatype=xsd.string)))
    g.add((subject, hasClass, Literal(row[1], datatype=xsd.integer)))
    g.add((subject, hasName, Literal(row[2], datatype=xsd.string)))
    g.add((subject, hasSex, Literal(row[3], datatype=xsd.string)))
    g.add((subject, hasAge, Literal(row[4], datatype=xsd.string)))
    g.add((subject, hasSibSp, Literal(row[5], datatype=xsd.string)))
    g.add((subject, hasParch, Literal(row[6], datatype=xsd.string)))
    g.add((subject, hasTicket, Literal(row[7], datatype=xsd.string)))
    g.add((subject, hasFare, Literal(row[8], datatype=xsd.string)))
    g.add((subject, hasCabin, Literal(row[9], datatype=xsd.string)))
    g.add((subject, hasEmbarked, Literal(row[10], datatype=xsd.string)))

# Save the graph to a TTL file
#g.serialize("output.ttl", format="turtle")
#g.serialize("graph2.ttl",format="turtle")  #print RDF/XML




ttl_data = BytesIO()
g.serialize(destination=ttl_data, format='turtle')
# Upload the TTL data to MinIO
minio_client =Minio(
    constants.MINIO_ENDPOINT,
    access_key=constants.MINIO_ACCESS_KEY,
    secret_key=constants.MINIO_SECRET_KEY,
    secure=False) 

# Reset the stream position to the beginning
ttl_data.seek(0)

# Upload TTL data to MinIO
minio_client.put_object(constants.MINIO_BUCKET_NAME_GRAPH, constants.MINIO_GRAPH_FILE, ttl_data, length=ttl_data.getbuffer().nbytes, content_type="text/turtle")

# Close Spark session
spark.stop()
