from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
You are a helpful assistant that is funny and always jokes about the user but still tries to help.
message from the user: {input}
the data form the user history conversation: {history}
"""

prompt = ChatPromptTemplate.from_template(template)


chain = prompt | model