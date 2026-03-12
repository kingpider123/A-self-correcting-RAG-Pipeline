from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load your text file
with open("source.txt", "r", encoding="utf-8") as f:
    text_data = f.read()

# 2. Configure your text splitter
# You want a chunk_size around 500, and chunk_overlap around 50
splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50) 

# 3. Create the chunks
chunks = splitter.create_documents([text_data])


# 4. Print the first 3 chunks to verify
for i in range(3):
    print(f"--- Chunk {i+1} ---")
    print(chunks[i].page_content)
    print("\n")