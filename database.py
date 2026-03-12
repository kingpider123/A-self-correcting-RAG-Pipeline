import chromadb
from chromadb.utils import embedding_functions

# 5. Initialize ChromaDB (this creates a local folder to store the database)
chroma_client = chromadb.PersistentClient(path="./rag_database")

# 6. Set up the embedding model (downloads automatically on first run)
embedding_model = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# 7. Create a collection (think of this as a table in SQL)
collection = chroma_client.get_or_create_collection(
    name="knowledge_base",
    embedding_function=embedding_model
)

# 8. Extract the text strings and create unique IDs for each chunk
documents = [chunk.page_content for chunk in chunks]
ids = [f"chunk_{i}" for i in range(len(chunks))]

# 9. Insert into the database
collection.add(
    documents=documents,
    ids=ids
)

print(f"Successfully embedded and stored {collection.count()} chunks in ChromaDB!")