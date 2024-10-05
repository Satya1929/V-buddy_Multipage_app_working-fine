#  pages/1_📂_Backend_Page.py (wroking fine , but have to upload all context pdfs before asking Q)


import streamlit as st
import google.generativeai as genai
import os
import PyPDF2

st.set_page_config(page_title="Backend Page", page_icon="📂")

st.title("Upload OCR-enabled PDF Files")
st.write("This is the backend page for developers to upload PDFs.")

# Fetch API key and configure generative AI
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if GOOGLE_API_KEY is None:
    st.error("API Key not found in environment variables")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Function to extract text from uploaded PDF files
def extract_text_from_pdfs(file_paths):
    text_content = []
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text_content.append(page.extract_text())
    return text_content

# Function to upload and verify multiple files
def upload_and_verify_files(file_paths):
    try:
        # Retrieve the list of existing files
        existing_files = genai.list_files()

        for file_path in file_paths:
            file_display_name = os.path.basename(file_path)
            sample_file = next((file for file in existing_files if file.display_name == file_display_name), None)

            if sample_file:
                st.warning(f"File '{file_display_name}' already exists, skipping upload.")
            else:
                sample_file = genai.upload_file(path=file_path, display_name=file_display_name)
                st.success(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

        # Extract text from uploaded PDFs and store in session state
        text_content = extract_text_from_pdfs(file_paths)
        st.session_state.uploaded_files_text = text_content

    except Exception as e:
        st.error(f"Failed to upload or verify files: {str(e)}")

# Streamlit UI for uploading files
uploaded_files_streamlit = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

if uploaded_files_streamlit:
    file_paths = []
    for uploaded_file in uploaded_files_streamlit:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(uploaded_file.name)

    upload_and_verify_files(file_paths)
