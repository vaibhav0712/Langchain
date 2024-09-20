from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server", version="1.0", description="Langchain Server API"
)

add_routes(app, ChatOpenAI(), path="/openai")

model_oepnai = ChatOpenAI()
# ollama model
model_ollama = Ollama(model="gemma:2b")

# prompts
prompt1 = ChatPromptTemplate.from_template(
    "write me an essay on {topic} around 100 wrods."
)
prompt2 = ChatPromptTemplate.from_template(
    "write me an poem on {topic} around 50 wrods."
)


add_routes(app, prompt1 | model_oepnai, path="/essay")
add_routes(app, prompt2 | model_ollama, path="/poem")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
