from model import chain
def chat(input: str, history: str = "") -> str:
    response = []
    """
    Chat with the assistant.

    Args:
        input (str): The user's input message.
        history (str, optional): The history of the conversation. Defaults to "".

    Returns:
        str: The assistant's response.
    """
    #response = chain.invoke({"input": input, "history": history})
    for text in chain.stream({"input": input, "history": history}):
        response.append(text)
    return response
