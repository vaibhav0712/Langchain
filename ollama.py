from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Prompt template
prompt_template = """
You are a helpful assistant.
{user_query}
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

# Streamlit framework
st.title("Langchain Ollama Chatbot")
input_text = st.text_input("Enter your query here")

# Call Ollama model here
llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({"user_query": input_text}))
