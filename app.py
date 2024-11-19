#from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from langchain import HuggingFaceHub


def get_hf_response(question):
    llm_hft = HuggingFaceHub(
        repo_id="google/flan-t5-large", 
        huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        model_kwargs={"temperature": 0, "max_length":64}
    )
    return llm_hft(question)

## function to load OpenAI model and get response

# def get_openai_response(question):
#     llm = OpenAI(
#         #model_name = "text-davinci-003"
#         temperature = 0.5,
#         openai_api_key = os.environ("OPENAI_API_KEY")
#     )
#     response = llm(question)
#     return response


## Initialize streamlit app


st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")
input = st.text_input("Input: ", key = "input")
submit = st.button("Submit")

## If submit button is clicked

if submit:
    response = get_hf_response(input)
    st.subheader("The response is: ")
    st.write(response)