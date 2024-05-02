from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, XSD

# Define namespaces
ex = Namespace("http://example.com/")
sh = Namespace("http://www.w3.org/ns/shacl#")

# Create an RDF graph
g = Graph()

# Add RDF triples
g.add((ex.Passenger, RDF.type, RDFS.Class))
g.add((ex.Passenger, RDFS.label, Literal("Passenger")))

properties = [
    (ex.hasAge, XSD.integer),
    (ex.hasCabin, XSD.string),
    (ex.hasClass, XSD.integer),
    (ex.hasEmbarked, XSD.string),
    (ex.hasFare, XSD.float),
    (ex.hasName, XSD.string),
    (ex.hasParch, XSD.integer),
    (ex.hasPassengerId, XSD.integer),
    (ex.hasSex, XSD.string),
    (ex.hasSibSp, XSD.integer),
    (ex.hasSurvived, XSD.boolean),
    (ex.hasTicket, XSD.string)
]

for prop, datatype in properties:
    g.add((prop, RDF.type, RDF.Property))
    g.add((prop, RDFS.label, Literal(str(prop).split("/")[-1])))
    g.add((prop, RDFS.domain, ex.Passenger))
    g.add((prop, RDFS.range, datatype))

# Create SHACL shape
shape = ex["PassengerShape"]
g.add((shape, RDF.type, sh.NodeShape))
g.add((shape, sh.targetClass, ex.Passenger))

for prop, datatype in properties:
    constraint = BNode()
    g.add((shape, sh.property, constraint))
    g.add((constraint, sh.path, prop))
    g.add((constraint, sh.datatype, datatype))

# Serialize to SHACL file (Turtle format)
shacl_file = "passenger_shape.shacl"
g.serialize(destination=shacl_file, format="turtle")

print(f"SHACL file created: {shacl_file}")
