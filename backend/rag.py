import os
import chromadb
from chromadb.utils import embedding_functions
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

CHROMA_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma")
os.makedirs(CHROMA_DIR, exist_ok=True)

client = chromadb.PersistentClient(path=CHROMA_DIR)
embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def get_collection(name: str = "pdf_chatmate"):
    return client.get_or_create_collection(
        name=name,
        embedding_function=embed_fn
    )

def index_chunks(chunks: List[Dict[str, str]], doc_name: str, collection_name: str = "pdf_chatmate"):
    collection = get_collection(collection_name)
    
    ids = [f"{doc_name}_{c['chunk_id']}" for c in chunks]
    documents = [c["text"] for c in chunks]
    metadatas = [{"source": doc_name, "chunk_id": c["chunk_id"]} for c in chunks]
    
    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

def query_rag(query: str, n_results: int = 3, collection_name: str = "pdf_chatmate") -> List[str]:
    collection = get_collection(collection_name)
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    if results and "documents" in results and results["documents"]:
        return results["documents"][0]
    return []