# pages/3_📝_Feedback_Page.py

import streamlit as st

st.set_page_config(page_title="Feedback Page", page_icon="📝")

# Page Title
st.title("We'd Love to Hear Your Feedback! 📝")

# Introductory Text
st.write("""
Your feedback helps us improve the Generative AI Q&A App. 
Please let us know your thoughts, suggestions, or any issues you've encountered.
""")

# Google Form Embedded in an iframe
st.write("### Please fill out the form below:")

google_form_url = "https://forms.gle/LAoy7nPvhYEdUe4y8"  # Replace with your Google Form link

# Display the form using iframe for a better visual experience
st.markdown(f"""
<iframe src="{google_form_url}" width="640" height="900" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
""", unsafe_allow_html=True)

# Closing Remarks
st.write("""
Thank you for your valuable feedback! Your input helps us make this app better.
""")

# st.snow() # A fun touch!


