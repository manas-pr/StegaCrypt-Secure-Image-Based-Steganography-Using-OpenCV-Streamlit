import cv2
import numpy as np
import streamlit as st
import os
from encrypt import encrypt_image  # Import encrypt function
from decrypt import decrypt_image  # Import decrypt function


# Streamlit UI
st.title("🔒 Image Steganography App")

# Sidebar options
st.sidebar.header("📌 Navigation")
option = st.sidebar.radio("Choose an option:", ("Encrypt Message", "Decrypt Message"))

# About section in the sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 About the Developer")
st.sidebar.markdown("""
**Manas Pratim Das**  
🎓 *MTech - Electronics and Communication Engineering*  
🤖 *Focus: Artificial Intelligence & Cyber Security*  

📌 **Connect with Me:**  
🔗 [LinkedIn](https://www.linkedin.com/in/manas-pratim-das-b95200197/)  
📧 **Email:** manas.pr94@gmail.com  
""")

# Encryption Section
if option == "Encrypt Message":
    st.subheader("Encrypt a Message into an Image")
    uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "png"])
    message = st.text_area("📝 Enter Secret Message")
    password = st.text_input("🔑 Set a Password", type="password")

    if st.button("🔐 Encrypt & Save"):
        if uploaded_file and message and password:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            encrypted_img = encrypt_image(img, message)
            cv2.imwrite("encryptedImage.png", encrypted_img)
            st.image("encryptedImage.png", caption="🔒 Encrypted Image", use_column_width=True)
            st.success("✅ Message Encrypted! Download the encrypted image below.")

            with open("encryptedImage.png", "rb") as f:
                st.download_button("📥 Download Encrypted Image", f, file_name="encryptedImage.png", mime="image/png")

        else:
            st.error("⚠ Please upload an image and enter a message.")

# Decryption Section
elif option == "Decrypt Message":
    st.subheader("Decrypt a Message from an Image")
    uploaded_file = st.file_uploader("📥 Upload Encrypted Image", type=["png", "jpg"])
    password = st.text_input("🔑 Enter Password", type="password")

    if st.button("🔓 Decrypt"):
        if uploaded_file and password:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            decrypted_msg = decrypt_image(img)  # No need for message length input
            st.success(f"✅ Decrypted Message: {decrypted_msg}")

        else:
            st.error("⚠ Please upload the encrypted image and enter the correct password.")

