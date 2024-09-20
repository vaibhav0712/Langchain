import requests
import streamlit as st


def get_openai_response(input_text):
    url = "http://localhost:8000/essay/invoke"
    payload = {"input": {"topic": input_text}}
    response = requests.post(url, json=payload)
    return response.json()["output"]


def get_ollama_response(input_text):
    url = "http://localhost:8000/poem/invoke"
    payload = {"input": {"topic": input_text}}
    response = requests.post(url, json=payload)
    return response.json()["output"]


st.title("Langchain Client")
input_text1 = st.text_input("Enter topic to generate essay (openai)")
input_text2 = st.text_input("Enter topic to generate poem (gemma:2b)")

if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))
