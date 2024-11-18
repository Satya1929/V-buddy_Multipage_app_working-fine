# pages/3_🎖_Credits_Page.py  (wroking fine , but have to upload all context pdfs before asking Q)

import streamlit as st

st.set_page_config(page_title="Credits Page", page_icon="🎖")

# Page Title
st.title("Credits 🎉")
st.write("Meet the amazing contributors behind this project:")

# Function to display a contributor's card with photo (from URL) and links
def display_contributor(name, linkedin_url, github_url, image_url):
    # Create a card-like structure with a photo in a circle
    st.markdown(f"""
    <div style="border: 2px solid #f1f1f1; padding: 20px; border-radius: 15px; margin-bottom: 20px; text-align: center;">
        <img src="{image_url}" alt="{name}'s photo" style="width: 150px; height: 150px; object-fit: cover; border-radius: 50%;">
        <h3>{name}</h3>
        <p>
            <a href="{linkedin_url}" target="_blank">LinkedIn</a> |
            <a href="{github_url}" target="_blank">GitHub</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Contributor 1 - Satyaprakash Swain
display_contributor(
    name="Satyaprakash Swain", 
    linkedin_url="https://www.linkedin.com/in/satyaprakash-swain-613067210/",
    github_url="https://github.com/Satya1929",
    image_url="https://avatars.githubusercontent.com/u/119441530?v=4"  # Replace with actual image URL
)

# Contributor 2 - Om Aditya
display_contributor(
    name="Om Aditya", 
    linkedin_url="www.linkedin.com/in/om-aditya-495312260",
    github_url="https://github.com/virtuoso8817",
    image_url="https://media.licdn.com/dms/image/v2/D5603AQGQw0y57m5GPw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1701676465547?e=1733356800&v=beta&t=SBs18AqHvhld2MmC9dnk_wGGCdoUDUHTRezDtVpaoA8"  # Replace with actual image URL
)

# Closing Note
st.write("We thank all contributors for their efforts and dedication to making this project a success!")

st.balloons()  # A fun touch!