# Main Execution of Program
from langchain_ollama import OllamaEmbeddings
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

# from langchain.messages import SystemMessage, HumanMessage

llm_name = "rwkv-7-g1d"
provider_url: str = "http://127.0.0.1:65530/api/oai"

embed_name = "nomic-embed-text"

model = ChatOpenAI(model=llm_name, base_url=provider_url, api_key=SecretStr("Mark 01"))
embed_model = OllamaEmbeddings(model=embed_name)

# single_vector = embed_model.embed_query("Hello, World!")
# print(str(single_vector)[:100])

print(model.invoke("Hello, World!"))

# print(embed_model.embed_query("Hello, World"))
# Prepare the content
# # Note: Ensure the text fits your model's context window!
# book_content = "The entire text of Pride and Prejudice..."
#
# messages = [
#     SystemMessage(
#         content=f"You are an AI assistant tasked with analyzing literary works. Context: {book_content}"
#     ),
#     HumanMessage(content="Analyze the major themes in 'Pride and Prejudice'."),
# ]
#
# # Standard invocation (Agents require 'tools', which you haven't defined)
# result = model.invoke(messages)
#
# print(result.content)
