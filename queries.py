from SPARQLWrapper import SPARQLWrapper, JSON

def run_sparql_query(sparql_endpoint, query):
    sparql = SPARQLWrapper(sparql_endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    try:
        results = sparql.query().convert()
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_results(results):
    if results and "results" in results and "bindings" in results["results"]:
        bindings = results["results"]["bindings"]
        if bindings:
            for result in bindings:
                print({k: v['value'] for k, v in result.items()})
        else:
            print("No results found.")
    else:
        print("No results found.")

if __name__ == "__main__":
    endpoint_url = "http://Elenis-MacBook-Air.local:7200/repositories/myDB"

    # Ask user to confirm the repository URL
    print(f"The current repository URL is: {endpoint_url}")
    user_response = input("Is this URL correct? (yes/no): ").strip().lower()

    # If the URL is not correct, request the user to provide the correct URL
    if user_response == 'no':
        endpoint_url = input("Please provide the correct repository URL: ").strip()

    print(f"The repository URL is now set to: {endpoint_url}")

    # SPARQL queries
    # Top Ten Authors by Book Count
    query1 = """
    PREFIX dc: <http://purl.org/dc/terms/>
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    PREFIX ex: <http://www.semanticweb.org/ontologies/2024/bookontology#>

    SELECT ?author (COUNT(?book) AS ?numBooks)
    WHERE {
      ?book a bibo:Book .
      ?book ex:writtenBy ?author .
    }
    GROUP BY ?author
    ORDER BY DESC(?numBooks)
    LIMIT 10
    """

    # Books Published Each Year
    query2 ="""
    PREFIX ns1: <http://www.semanticweb.org/ontologies/2024/bookontology#>
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    
    SELECT ?year (COUNT(?book) AS ?numBooks)
    WHERE {
      ?book a bibo:Book ;
            ns1:publicationYear ?year .
    }
    GROUP BY ?year
    ORDER BY ?year
    """

    # Books with High Average Ratings
    query3 = """
    PREFIX dc: <http://purl.org/dc/terms/>
    PREFIX bibo: <http://purl.org/ontology/bibo/>
    PREFIX ex: <http://www.semanticweb.org/ontologies/2024/bookontology#>

    SELECT ?book (AVG(?ratingValue) AS ?averageRating)
    WHERE {
    ?rating a ex:Ratings;
            ex:ratesBook ?book;
            ex:ratingValue ?ratingValue.
    OPTIONAL {?book dc:title ?title.}
    }
    GROUP BY ?book
    HAVING (AVG(?ratingValue) > 8)
    ORDER BY DESC(?averageRating)
    """

    # Run queries
    print("Query 1 Results (Authors and Number of Books):")
    results1 = run_sparql_query(endpoint_url, query1)
    display_results(results1)

    print("\nQuery 2 Results (Books Published Each Year):")
    results2 = run_sparql_query(endpoint_url, query2)
    display_results(results2)

    print("\nQuery 3 Results (Books with High Average Ratings):")
    results3 = run_sparql_query(endpoint_url, query3)
    display_results(results3)