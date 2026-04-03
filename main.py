from vectorstore import add_document_to_vectorstore
from chat import chat


while True:
    input_text = input("Enter your message (Enter 'exit' to quit): ")
    if input_text == "exit":
        break
    add_document_to_vectorstore(input_text)
    retrieval = retrieve_document(input_text)
    chat_response = chat(input_text, retrieval)
    print(chat_response)