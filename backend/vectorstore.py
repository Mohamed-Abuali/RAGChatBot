from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
import os

# Global variables to hold the vector store and embeddings to avoid re-initializing.
_vectorstore = None
_embeddings = None

def get_embeddings():
    """
    Initializes and returns the Ollama embeddings model.
    """
    global _embeddings
    if _embeddings is None:
        _embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    return _embeddings

def get_vectorstore():
    """
    Initializes and returns the Chroma vector store.
    """
    global _vectorstore
    if _vectorstore is None:
        vector_location = "./vectorstore"
        _vectorstore = Chroma(
            collection_name="rag_chat",
            embedding_function=get_embeddings(),
            persist_directory=vector_location,
        )
    return _vectorstore

def get_retriever():
    """
    Creates and returns a retriever from the vector store.
    """
    vectorstore = get_vectorstore()
    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5},
    )
        