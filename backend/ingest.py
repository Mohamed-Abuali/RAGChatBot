from langchain_core.documents import Document
from .vectorstore import get_vectorstore

def main():
    """
    Main function to ingest documents into the vector store.
    """
    # For this example, we'll add some dummy documents.
    # In a real application, you would load these from files (PDF, TXT, etc.).
    print("Ingesting documents into the vector store...")
    texts = [
        "The sky is blue.",
        "The grass is green.",
        "The sun is bright.",
        "LangChain is a framework for developing applications powered by language models.",
        "Chroma is an open-source embedding database.",
        "Ollama allows you to run large language models locally."
    ]
    documents = [Document(page_content=t) for t in texts]
    
    vectorstore = get_vectorstore()
    vectorstore.add_documents(documents)
    print("Documents ingested successfully!")

if __name__ == "__main__":
    main()
