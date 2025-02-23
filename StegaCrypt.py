import cv2
import numpy as np
import streamlit as st
import os


# Set background image using CSS
page_bg_img = """
<style>
.stApp {
    background-image: url("https://img.freepik.com/free-photo/abstract-techno-background-with-connecting-lines_1048-5570.jpg?t=st=1740335237~exp=1740338837~hmac=a27f074d10a82ab100c989421ad79ec1d088b29b6f0d5a7f5f5412ff5bb4c967&w=996");
    background-size: cover;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Streamlit UI
st.title("🔒 StegaCrypt - Image Steganography App")

# Sidebar options
st.sidebar.header("📌 Navigation")
option = st.sidebar.radio("Choose an option:", ("Encrypt Message", "Decrypt Message"))

# About section in the sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 About the Developer")
st.sidebar.markdown("""
**Manas Pratim Das**  
🎓 *Electronics and Communication Engineering (MTech/MS)*  
🤖 *Focus Areas:*  
       ✅ Artificial Intelligence & Machine Learning  
       ✅ Deep Learning & Secure Computing  
       ✅ Neuromorphic Computing  

📌 **Connect with Me:**  
🔗 [LinkedIn](https://www.linkedin.com/in/manas-pratim-das-b95200197/)  
📧 [Email](mailto:manas.pr94@gmail.com)
🐙 [GitHub](https://github.com/manas-pr)  
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

            encrypted_img = encrypt_image(img, message)  # Ensure encrypt_image() is defined
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

            decrypted_msg = decrypt_image(img)  # Ensure decrypt_image() is defined
            st.success(f"✅ Decrypted Message: {decrypted_msg}")

        else:
            st.error("⚠ Please upload the encrypted image and enter the correct password.")
