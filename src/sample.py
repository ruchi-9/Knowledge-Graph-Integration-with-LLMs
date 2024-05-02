from pyspark.sql import SparkSession
from rdflib import Graph, Literal, URIRef

# Create a SparkSession
spark = SparkSession.builder \
    .appName("PopulateGraph") \
    .getOrCreate()

# Load CSV file into DataFrame
csv_file_path = "/home/ruchi/Desktop/DE_Project/titanic.csv"
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Create an RDF graph
g = Graph()

# Iterate through DataFrame rows and add triples to the graph
for row in df.collect():
    subject = URIRef(f"http://example.org/{row['Sex']}")
    predicate = URIRef(f"http://example.org/{row['Survived']}")
    object_value = Literal(row['PassengerId'])
    g.add((subject, predicate, object_value))

# Define the graph file path
graph_file_path = "populated_graph.ttl"

# Serialize the graph to TTL format and save to file
g.serialize(graph_file_path, format='turtle')

# Stop SparkSession
spark.stop()
