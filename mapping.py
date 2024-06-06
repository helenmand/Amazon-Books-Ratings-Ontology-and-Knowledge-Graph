from pyrml import RMLConverter
import os
from rdflib import Graph

test_graph = Graph()
try:
    with open("rules.ttl", 'r') as f:  
        test_graph.parse("rules.ttl", format="turtle") 
    print("RML file is syntactically correct.")
except Exception as e:
    print(f"Error found: {e}")

# Create an instance of the class RMLConverter.
rml_converter = RMLConverter()

rml_file_path = os.path.join('', 'rules.ttl')
rdf_graph = rml_converter.convert(rml_file_path)

output_ttl_path = "result.ttl"
rdf_graph.serialize(destination=output_ttl_path, format="turtle")
print(f"RDF triples have been saved to {output_ttl_path}")