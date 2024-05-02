# Driver import
from neo4j import GraphDatabase
# Replace with the actual URI, username and password
AURA_CONNECTION_URI = "bolt://localhost:7474"
AURA_USERNAME = "neo4j"
AURA_PASSWORD = "neo4j1234"

# Driver instantiation
driver = GraphDatabase.driver(
    AURA_CONNECTION_URI,
    auth=(AURA_USERNAME, AURA_PASSWORD)
)