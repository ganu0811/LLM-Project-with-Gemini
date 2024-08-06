from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('Google_Gemini_API_key'))


# function to load gemini pro model to get responses

model = genai.GenerativeModel('gemini-pro')

def get_gemini_responses(question):
    response = model.generate_content(question)
    return response.text


# initializing our streamlit app

st.set_page_config(page_title = " Q&A Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input: ", key = 'input')

submit = st.button("Ask the question")

#When submit is clicked

if submit:
    response = get_gemini_responses(input)
    st.subheader('The Response is:')
    st.write(response) 
    