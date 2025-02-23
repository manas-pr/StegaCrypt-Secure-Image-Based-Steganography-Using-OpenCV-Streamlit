import streamlit as st
from encrypt import encrypt_message
from decrypt import decrypt_message
import os

st.title("StegaCrypt: Image Steganography")

option = st.radio("Choose an option:", ["Encrypt", "Decrypt"])

if option == "Encrypt":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    message = st.text_area("Enter secret message")
    
    if st.button("Encrypt"):
        if uploaded_file and message:
            image_path = "input_image.png"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            encrypted_path = encrypt_message(image_path, message)
            st.image(encrypted_path, caption="Encrypted Image", use_column_width=True)
            st.success("Message encrypted successfully!")

elif option == "Decrypt":
    uploaded_file = st.file_uploader("Upload the encrypted image", type=["png", "jpg", "jpeg"])
    length = st.number_input("Enter message length", min_value=1, step=1)

    if st.button("Decrypt"):
        if uploaded_file:
            image_path = "encrypted_image.png"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            decrypted_message = decrypt_message(image_path, length)
            st.text_area("Decrypted Message:", decrypted_message)
            st.success("Decryption successful!")
