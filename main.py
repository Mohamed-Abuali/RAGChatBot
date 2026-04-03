from vectorstore import add_document_to_vectorstore
from chat import chat


while True:
    input_text = input("Enter your message (Enter 'exit' to quit): ")
    if input_text == "exit":
        break
    retrieval = add_document_to_vectorstore(input_text).invoke(input_text)
    chat_response = chat(input_text, retrieval)
    print(chat_response)