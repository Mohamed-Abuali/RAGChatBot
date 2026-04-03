from vectorstore import add_a_document, retrieve_document
from chat import chat


while True:
    input_text = input("Enter your message (Enter 'exit' to quit): ")
    if input_text == "exit":
        break
    add_a_document(input_text)
    retrieval = retrieve_document(input_text)
    for chat_response in chat(input_text, retrieval):
        add_a_document(chat_response)
        print(chat_response, end=" ")
