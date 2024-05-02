from rdflib import Graph, Namespace, RDF, RDFS, XSD, Literal


# Create a new RDF Graph
g = Graph()

# Define Namespace
ex = Namespace("http://example.com/")
g.bind("ex", ex)

# Define Classes
g.add((ex.Passenger, RDF.type, RDFS.Class))
g.add((ex.Passenger, RDFS.label, Literal("Passenger")))

# Define Properties
properties = [
    (ex.hasPassengerId, "has PassengerId", XSD.integer),
    (ex.hasSurvived, "has Survived", XSD.boolean),
    (ex.hasClass, "has Class", XSD.integer),
    (ex.hasName, "has Name", XSD.string),
    (ex.hasSex, "has Sex", XSD.string),
    (ex.hasAge, "has Age", XSD.integer),
    (ex.hasSibSp, "has Siblings/Spouses", XSD.integer),
    (ex.hasParch, "has Parents/Children", XSD.integer),
    (ex.hasTicket, "has Ticket", XSD.string),
    (ex.hasFare, "has Fare", XSD.float),
    (ex.hasCabin, "has Cabin", XSD.string),
    (ex.hasEmbarked, "has Embarked", XSD.string)
]

for prop, label, datatype in properties:
    g.add((prop, RDF.type, RDF.Property))
    g.add((prop, RDFS.label, Literal(label)))
    g.add((prop, RDFS.domain, ex.Passenger))
    g.add((prop, RDFS.range, datatype))

# Serialize the RDF Graph to Turtle format and print it
print(g.serialize("schema.ttl",format="turtle"))


