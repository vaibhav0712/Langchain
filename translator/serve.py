from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

# Create model 
model_groq = ChatGroq(model='llama3-8b-8192')
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
print(os.getenv('GROQ_API_KEY'))


# Create Prompt Template 
system_prompt = "Translate the following into {language}"
prompt = ChatPromptTemplate.from_messages([('system',system_prompt),('user','{text}')])

# Create output parser
parser = StrOutputParser()


# Create Chain
chain = prompt| model_groq | parser

# App definiton 

app = FastAPI(
    title='Langchain Server',
    version='1.0',
    description='Langchain Server API'
)


# Add chain to route 

add_routes(
    app,
    chain,
    path='/translate'
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='localhost',port=8000)