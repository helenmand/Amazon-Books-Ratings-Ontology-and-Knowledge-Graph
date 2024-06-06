from rdflib import Graph, URIRef, RDF, Namespace
import requests

EX = Namespace('http://www.semanticweb.org/ontologies/2024/bookontology#')
BIBO = Namespace('http://purl.org/ontology/bibo/')

def clear_graphdb(endpoint):
    try:
        response = requests.delete(endpoint)
        if response.status_code == 204:
            print("GraphDB repository cleared.")
        else:
            print(f"Failed to clear GraphDB repository: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Error clearing GraphDB repository: {e}")

def add_data_to_graphdb(repository_url, data, data_type="data"):
    headers = {"Content-Type": "application/x-turtle"}
    response = requests.post(f"{repository_url}/statements", headers=headers, data=data)
    
    if response.status_code == 204:
        print(f"{data_type.capitalize()} successfully added to GraphDB.")
    else:
        print(f"Failed to add {data_type} to GraphDB: {response.status_code} - {response.reason}")

def serialize_data(graph, subject):
    # Serialize the triples concerning the subject (user or rating or book)
    new_graph = Graph()
    
    for predicate, obj in graph.predicate_objects(subject=subject):
        new_graph.add((subject, predicate, obj))
    
    return new_graph.serialize(format='turtle')

def load_data_serially(repository_url, turtle_file_path, class_uri):
    graph = Graph()
    graph.parse(turtle_file_path, format='turtle')

    for subject in graph.subjects(predicate=RDF.type, object=class_uri):
        data = serialize_data(graph, subject)
        add_data_to_graphdb(repository_url, data, class_uri.split('/')[-1])

if __name__ == "__main__":
    graphdb_repository_url = "http://Elenis-MacBook-Air.local:7200/repositories/myDB"
    turtle_file_path = 'result.ttl'

    # Ask user to confirm the repository URL
    print(f"The current repository URL is: {graphdb_repository_url}")
    user_response = input("Is this URL correct? (yes/no): ").strip().lower()

    # If the URL is not correct, request the user to provide the correct URL
    if user_response == 'no':
        graphdb_repository_url = input("Please provide the correct repository URL: ").strip()

    print(f"The repository URL is now set to: {graphdb_repository_url}")
    print(f"The turtle file path is: {turtle_file_path}")

    graphdb_endpoint = f"{graphdb_repository_url}/statements"
    clear_graphdb(graphdb_endpoint) # optional - used when testing
    
    # Define RDF types for books, users, and ratingsx
    rdf_book_type = URIRef('http://purl.org/ontology/bibo/Book')
    rdf_user_type = EX.Users 
    rdf_rating_type = EX.Ratings

    # Load books and ratings serially
    load_data_serially(graphdb_repository_url, turtle_file_path, rdf_book_type)
    load_data_serially(graphdb_repository_url, turtle_file_path, rdf_rating_type)
    load_data_serially(graphdb_repository_url, turtle_file_path, rdf_user_type)