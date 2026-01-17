import os
import PyPDF2
import streamlit as st

def extract_text_from_pdf(file_path):
    """Extracts text from a single PDF file."""
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return text

def load_all_pdfs(directory):
    """Recursively finds all PDFs in a directory and extracts their text."""
    all_text = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".pdf"):
                file_path = os.path.join(root, file)
                text = extract_text_from_pdf(file_path)
                if text:
                    all_text.append(text)
    return all_text

def get_all_pdf_texts():
    """Returns all PDF texts, using session state for caching."""
    # Define the base directory for PDFs
    base_dir = "Database PDFs"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    if 'uploaded_files_text' not in st.session_state or not st.session_state.uploaded_files_text:
        if os.path.exists(base_dir):
            with st.spinner("Loading database PDFs..."):
                st.session_state.uploaded_files_text = load_all_pdfs(base_dir)
        else:
            st.session_state.uploaded_files_text = []
    return st.session_state.uploaded_files_text
