from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

# Global variables to hold the chain and its components to avoid re-initializing.
_model = None
_prompt = None
_chain = None

def get_chain() -> Runnable:
    """
    Initializes and returns the LangChain chain.
    This function ensures that the chain is only created once.
    """
    global _chain, _prompt, _model
    if _chain is None:
        template = """
        You are a helpful assistant that is funny and always jokes about the user but still tries to help.
        message from the user: {input}
        the data form the user history conversation: {history}
        """
        _prompt = ChatPromptTemplate.from_template(template)


        _model = OllamaLLM(
            model="llama3.2",
            temperature=0.7,
            num_predict=1024,
        )

        _chain = _prompt | _model
    return _chain