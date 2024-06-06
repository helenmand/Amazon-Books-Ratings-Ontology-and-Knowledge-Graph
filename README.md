# Amazon-Books-Ratings-Ontology-and-Knowledge-Graph
This project aims to create an ontology based on a dataset of Amazon book ratings, map the dataset into RDF triples using RML, and upload the triples into a graph database (GraphDB) to perform SPARQL queries.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/helenmand/Amazon-Books-Ratings-Ontology-and-Knowledge-Graph.gitt
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. **Define the Ontology** in the `book_ontology.ttl` file. 

2. **Map the Dataset** using the `mapping.py` script to map the dataset into RDF triples. 

3. **Generate RDF Triples**, the `result.ttl` file, generated from the `mapping.py` file, contains the RDF triples generated from the dataset. This file is used to upload the data into the graph database.

4. **Upload to Graph Database** using the `graphdb_build.py` script to upload the RDF triples into the graph database (GraphDB).
     
## Links
- [Amazon Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset)
- [pyRML](https://github.com/anuzzolese/pyrml)
- [GraphDB](https://www.ontotext.com/products/graphdb/download/)

