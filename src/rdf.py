# Driver import
from neo4j import GraphDatabase
import rdflib
# Replace with the actual URI, username and password
AURA_CONNECTION_URI = "bolt://localhost:7474"
AURA_USERNAME = "neo4j"
AURA_PASSWORD = "neo4j1234"

# Driver instantiation

def import_ttl_to_neo4j(ttl_file):
    # Load TTL file into an RDF Graph
    g = rdflib.Graph()
    g.parse(ttl_file, format='turtle')

    # Connect to Neo4j
    #driver = GraphDatabase.driver(uri, auth=(username, password))
    driver = GraphDatabase.driver(AURA_CONNECTION_URI,auth=(AURA_USERNAME, AURA_PASSWORD))
    
    # Create Neo4j session
    with driver.session() as session:
        # Iterate over each triple in the RDF graph
        for subject, predicate, obj in g:
            # Convert RDF nodes to strings
            subject_str = str(subject)
            predicate_str = str(predicate)
            object_str = str(obj)

            # Create nodes and relationships in Neo4j
            session.run(
                """
                MERGE (s:Node {id: $subject})
                MERGE (o:Node {id: $object})
                MERGE (s)-[:RELATIONSHIP {type: $predicate}]->(o)
                """,
                subject=subject_str,
                object=object_str,
                predicate=predicate_str
            )

    # Close Neo4j driver
    driver.close()

# Example usage
ttl_file = "/home/ruchi/Downloads/graph2.ttl"
import_ttl_to_neo4j(ttl_file)