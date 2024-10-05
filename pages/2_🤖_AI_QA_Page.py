# pages/2_🤖_AI_QA_Page.py

import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="AI Q&A Page", page_icon="🤖")

st.title("Generative AI Q&A System")
st.write("Ask a question, and the model will respond based on the uploaded files.")

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if GOOGLE_API_KEY is None:
    st.error("API Key not found in environment variables")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Retrieve the uploaded files' text from session state
if 'uploaded_files_text' in st.session_state:
    uploaded_files_text = st.session_state.uploaded_files_text
else:
    uploaded_files_text = []

# Input box for user questions
user_input = st.text_input("You: ", placeholder="Type 'exit' to stop.")

if user_input:
    if user_input.lower() == 'exit':
        st.write("Exiting the conversation.")
    else:
        try:
            prompt = [user_input] + uploaded_files_text  # Include extracted text in the prompt
            response = model.generate_content(prompt)
            st.write(f"Model: {response.text}")
        except Exception as e:
            st.error(f"Failed to generate content: {str(e)}")
