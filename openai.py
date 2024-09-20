from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt_template = """
You are a helpful assistant.
{user_query}
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

# Streamlit framework
st.title("Langchain OpenAI Chatbot")
input_text = st.text_input("Enter your query here")


# Open AI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({"user_query": input_text}))
