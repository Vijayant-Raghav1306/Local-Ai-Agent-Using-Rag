# 1. CHANGE THE IMPORT
# Old: from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd
from dotenv import load_dotenv # Don't forget this!

# 2. LOAD PASSWORDS
load_dotenv()

df = pd.read_csv("realistic_restaurant_reviews.csv")

# 3. CHANGE THE MODEL
# Old: embeddings = OllamaEmbeddings(model="mxbai-embed-large")
# New: You MUST use an embedding model, NOT a chat model like gemini-flash
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    print("Creation started...")
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )
    vector_store.add_documents(documents=documents, ids=ids)
    print("✅ Database created successfully!")

else:
    print("Database already exists. Loading...")
    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)




