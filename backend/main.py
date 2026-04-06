from vectorstore import add_a_document, retrieve_document
from chat import chat
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    input_text = data.get("input_text")
    if input_text == "exit":
        return JSONResponse(content={"message": "Exiting chat"})
    add_a_document(input_text)
    retrieval = retrieve_document(input_text)
    response = ""
    for chat_response in chat(input_text, retrieval):
        add_a_document(chat_response)
        response += chat_response
    return JSONResponse(content={"message": response})

# while True:
#     try:
#         input_text = input("\nEnter your message (Enter 'exit' to quit): \n")
#         if input_text == "exit":
#             break
#         add_a_document(input_text)
#         retrieval = retrieve_document(input_text)
#         print("\nAssistant:", end="")
#         for chat_response in chat(input_text, retrieval):
#             add_a_document(chat_response)
#             print(chat_response, end="")
#     except Exception as e:
#         print(f"Error: {e}")
