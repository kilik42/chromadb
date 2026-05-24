import chromadb

chroma_client = chromadb.Client()

collection_name = "my_collection"

collection = chroma_client.get_or_create_collection(name="my_collection")

#text collections 

# Define text documents
documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
]

# add documents to the collection
# collection.add(documents)

for doc in documents:
    collection.upsert(ids=[doc["id"]], documents=[doc["text"]])

query_text = "What is the greeting in doc1?"

results = collection.query(
    query_texts=[query_text],
    n_results=3,
)

# print(results)
for idx, result in enumerate(results["documents"][0]):
    # print(f"Result {idx + 1}: {result}")
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    # embedding = results["embeddings"][0][idx]
    print(f"Result {idx + 1}: Document ID: {doc_id}, Distance: {distance}, Text: {result}")