# pages/1_📂_Backend_Page.py

import streamlit as st
import google.generativeai as genai
import os
from utils import get_all_pdf_texts

st.set_page_config(page_title="Backend Page", page_icon="📂")

st.title("Settings & Knowledge Base")
st.write("Upload PDF files to permanently add them to the AI's knowledge base.")

# Fetch API key and configure generative AI
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if GOOGLE_API_KEY is None:
    st.error("API Key not found in environment variables")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Define Database directory
DB_DIR = "Database PDFs"
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

# Function to upload and verify multiple files with Google AI (Optional but kept for compatibility)
def upload_to_gemini_cloud(file_paths):
    try:
        existing_files = genai.list_files()
        for file_path in file_paths:
            file_display_name = os.path.basename(file_path)
            sample_file = next((file for file in existing_files if file.display_name == file_display_name), None)

            if sample_file:
                st.info(f"File '{file_display_name}' already exists in Gemini Cloud.")
            else:
                sample_file = genai.upload_file(path=file_path, display_name=file_display_name)
                st.success(f"Cloud Upload: '{sample_file.display_name}'")
    except Exception as e:
        st.warning(f"Note: Cloud upload to Gemini failed (API might be restricted): {str(e)}")

# Streamlit UI for uploading files
uploaded_files_streamlit = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

if uploaded_files_streamlit:
    file_paths = []
    for uploaded_file in uploaded_files_streamlit:
        # Save to local persistent storage
        dest_path = os.path.join(DB_DIR, uploaded_file.name)
        with open(dest_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(dest_path)

    # Cloud upload (optional, kept from original code)
    upload_to_gemini_cloud(file_paths)
    
    # Reset session state so the Q&A page reloads the new database
    if 'uploaded_files_text' in st.session_state:
        del st.session_state.uploaded_files_text
    
    st.success(f"Successfully added {len(file_paths)} files to the database!")
    st.info("You can now go to the AI Q&A Page to ask questions about these documents.")

# Show currently loaded files
st.divider()
st.subheader("Current Database Files")
all_files = []
for root, dirs, files in os.walk(DB_DIR):
    for file in files:
        if file.lower().endswith(".pdf"):
            all_files.append(os.path.join(root, file))

if all_files:
    for f in all_files:
        st.text(f"📄 {os.path.relpath(f, DB_DIR)}")
else:
    st.write("No files in database yet.")
