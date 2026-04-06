from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .chat import chat
from .vectorstore import get_retriever

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    input_text = data.get("input")
    retriever = get_retriever()
    retrieval = retriever.invoke(input_text)
    response = chat(input_text, retrieval)
    return JSONResponse(content={"message": response})

