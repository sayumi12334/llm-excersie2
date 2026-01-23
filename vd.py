# %%
# populating for ChromaDB

import chromadb

ch_client = chromadb.Client()
collection =ch_client.create_collection(name="test_collection")
collection.add(
   documents=[
       "This is a document about BMI",
       "This is a document about blood pressure ",
       "This is a document about Complete Blood Count (CBC) "
   ],
   metadatas=[
       {"source": "test 1"},
       {"source": "test2"},
       {"source": "test3"}
   ],
   ids=[
       "b1",
       "b2",
       "b3"
   ]
)


# %%
# Query for ChromaDB
results = collection.query(
    query_texts=["This is a query about CBC and BMI"],
    n_results=3
)
print(results)

# %%
