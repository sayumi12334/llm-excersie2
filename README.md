# 1. Vector Databases
## Why vector databases ?
Vector databases are used to find data based on similarity in meaning, not just exact keyword matching like in relational databases. This helps avoid missing the right results when the wording is different while searching. A vector database stores data as embeddings (dense numeric vectors that represent text, images, audio, etc.), and it searches by comparing how close those vectors are using similarity measures (cosine similarity, Euclidean distance etc.). Because of this, it can retrieve items that are semantically similar  or visually similar . This is  useful for things like image and video search, recommendation systems, and fraud detection.

## For ChromaDB
### How to populate
First, create a Chroma client, which acts as the connection to the Chroma database. Then, create a collection, which is where Chroma stores the documents, their embeddings , and metadata. To populate the collection, use collection.add() to insert the data by providing ids (unique string labels for each document), documents (the actual text you want to store), and metadatas(optional). 

### How to query
Use collection.query() and pass query_texts (the text you want to search with). Chroma converts  query_texts  into an embedding and compares it with the embeddings of the stored documents. Then set n_results to choose how many of the most similar matches you want to be returned.

### What are the other vector databases people use
Pinecone, deeplake , vespa, Milvus , scaNN 

# 2. RAG
## Why RAG
RAG is used because LLMs on their own can generate outdated answers or answers based on unreliable resources.  With RAG, the system first retrieves relevant, reliable information ( from vector databases, documents, the  web etc) based on the user’s question, and then the LLM uses that retrieved information to generate the final response. This ensures that the answers are more accurate, more up to date, and more relevant to the user’s question

##  Basic RAG  architecture
 A client sends a question to a RAG framework . The framework turns the question into an embedding and performs semantic search in a vector database to find the most revelant documents that match the query. The framework builds a prompt using  the user’s question and the retrieved context and sends it to the LLM. The LLM generates an answer based on the built in knowledge of the model with th emost recent information retrieved.