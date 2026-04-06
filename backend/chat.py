from .model import get_chain
def chat(input: str, history: str = "") -> str:
    chain = get_chain()
    response = ""
    for text in chain.stream({"input": input, "history": history}):
        response += text
    return response
