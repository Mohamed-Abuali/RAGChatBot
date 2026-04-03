from model import chain
def chat(input: str, history: str = "") -> str:
    """
    Chat with the assistant.

    Args:
        input (str): The user's input message.
        history (str, optional): The history of the conversation. Defaults to "".

    Returns:
        str: The assistant's response.
    """
    response = chain.invoke({"input": input, "history": history})
    return response
