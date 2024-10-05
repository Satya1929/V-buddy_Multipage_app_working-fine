# Main.py

import streamlit as st

st.set_page_config(
    page_title="V-Buddy App",
    page_icon="🤖",
)

st.write("# Welcome to the Generative AI QnA App! 🤖")
st.sidebar.success("Select a page from the sidebar to navigate.")

st.markdown("""
    This application allows users to ask questions to a Generative AI model 
    based on uploaded context PDFs. Navigate to the appropriate page to begin!
    
    ### Pages Available:
    - 📂 **Backend Page**: Developers can upload PDFs here.
    - 🤖 **AI Q&A Page**: Users can interact with the Generative AI with context of uploaded files.
    - 📝 **Feedback Page**: Users can provide feedback for improvement.
    - 🎉 **Credits Page**: Anyone can see the contributors of the V-Buddy
""")
