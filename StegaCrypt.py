import cv2
import numpy as np
import streamlit as st
import os
import tempfile
from encrypt import encrypt_image # Import encryption function
from decrypt import decrypt_image # Import decryption function
# Set background image and selective text styling using CSS
page_bg_img = """
<style>
.stApp {
 background-image: url("https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/deep-learning-visual.png");
 background-size: cover;
 background-attachment: fixed;
}
/* Make the main title and subheadings white */
h1, h2 {
 color: white !important;
 text-align: center;
}
/* Set specific labels to white */
div[data-testid="stFileUploader"] label,
div[data-testid="stTextInput"] label,
div[data-testid="stTextArea"] label {
 color: white !important;
 font-weight: bold;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# Streamlit UI
st.markdown("<h1>🔒 StegaCrypt - Secure Image Steganography App</h1>", unsafe_allow_html=True)
# Sidebar options
st.sidebar.header("📌 Navigation")
option = st.sidebar.radio("Choose an option:", ("Encrypt Message", "Decrypt Message"))
# About section in the sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 About the Developer")
st.sidebar.markdown("""
**Manas Pratim Das**
