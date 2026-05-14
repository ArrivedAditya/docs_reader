# Main Execution of Program

from langchain_openai import ChatOpenAI
from pydantic.types import SecretStr

llm_name: str = "rwkv7-g1d"
provider_url: str = "http://192.168.29.174:52345/v1"

model = ChatOpenAI(model=llm_name, base_url=provider_url, api_key=SecretStr("Mark 01"))
print(model.invoke("Hello, World!"))
