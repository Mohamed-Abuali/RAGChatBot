from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
import os


embeddings = OllamaEmbeddings(model="mxbai-embed-large")

vector_location = "./vectorstore"
add_document = not os.path.exists(vector_location)
vectorstore = Chroma(
            collection_name="rag_chat",
            embedding_function=embeddings,
            persist_directory=vector_location,
    )
def add_a_document(document) -> None:
    """
    Add a document to the vectorstore.

    Args:
        document (str): The document to add.
    """
    documents = []
    ids = []
    if add_document:
        documents.append(
            Document(
                page_content=document,
                metadata={"source": "local"},
                id=str(len(document)),
                )
            )
        ids.append(str(len(document)))
    if add_document:
        vectorstore.add_documents(documents)
    
    
def retrieve_document(query: str):
    """
    Retrieve a document from the vectorstore.

    Args:
        query (str): The query to retrieve.
    """
    retrieval = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5},
    )
    return retrieval.invoke(query)

        