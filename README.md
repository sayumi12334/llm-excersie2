# 1. Vector Databases
## Why vector databases ?
Vector databases are used to find data based on similarity in meaning, not just exact keyword matching like in relational databases. This helps avoid missing the right results when the wording is different while searching. A vector database stores data as embeddings (dense numeric vectors that represent text, images, audio, etc.), and it searches by comparing how close those vectors are using similarity measures (cosine similarity, Euclidean distance etc.). Because of this, it can retrieve items that are semantically similar  or visually similar . This is  useful for things like image and video search, recommendation systems, and fraud detection.

## For ChromaDB
### How to populate
First, create a Chroma client, which acts as the connection to the Chroma database. Then, create a collection, which is where Chroma stores the documents, their embeddings , and metadata. To populate the collection, use collection.add() to insert the data by providing ids (unique string labels for each document), documents (the actual text you want to store), and metadatas(optional). 

### How to query
Use collection.query() and pass query_texts (the text you want to search with). Chroma converts  query_texts  into an embedding and compares it with the embeddings of the stored documents. Then set n_results to choose how many of the most similar matches you want to be returned.