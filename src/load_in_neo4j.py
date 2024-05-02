from py2neo import Graph, Node, Relationship

# Neo4j credentials and configuration
NEO4J_URI = "http://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "neo4j"

# Path to the TTL file
TTL_FILE_PATH = "/home/ruchi/Downloads/graph2.ttl"

# Connect to Neo4j
graph = Graph(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Load TTL file into Neo4j
with open(TTL_FILE_PATH, "r") as file:
    ttl_data = file.read()

    # Run Cypher query to load TTL data
    query = """CALL n10s.rdf.import.inline("{}","Turtle")""".format(ttl_data)

    graph.run(query)

print("TTL file loaded into Neo4j.")
