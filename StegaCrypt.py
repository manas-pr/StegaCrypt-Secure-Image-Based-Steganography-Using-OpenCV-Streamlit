import cv2
import numpy as np
import streamlit as st
from encrypt import encrypt_image  # Import updated encrypt function
from decrypt import decrypt_image  # Import updated decrypt function

# Set background image using CSS
page_bg_img = """
<style>
.stApp {
    background-image: url("https://img.freepik.com/free-photo/abstract-techno-background-with-connecting-lines_1048-5570.jpg?t=st=1740339735~exp=1740343335~hmac=9cc6cf6a2b6f19cde9482a63d682c36fd20818686ef7789a5fe7124e0dcd4753&w=1380");
    background-size: cover;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit UI
st.title("🔒 StegaCrypt - Secure Image Steganography")

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
🐙 [GitHub](https://github.com/manas-pr)  
📧 [Email](mailto:manas.pr94@gmail.com)   
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

            encrypted_img = encrypt_image(img, message, password)  # Updated function with password
            cv2.imwrite("encryptedImage.png", encrypted_img)
            st.image("encryptedImage.png", caption="🔒 Encrypted Image", use_column_width=True)
            st.success("✅ Message Encrypted! Download the encrypted image below.")

            with open("encryptedImage.png", "rb") as f:
                st.download_button("📥 Download Encrypted Image", f, file_name="encryptedImage.png", mime="image/png")

        else:
            st.error("⚠ Please upload an image, enter a message, and set a password.")

# Decryption Section
elif option == "Decrypt Message":
    st.subheader("Decrypt a Message from an Image")
    uploaded_file = st.file_uploader("📥 Upload Encrypted Image", type=["png", "jpg"])
    password = st.text_input("🔑 Enter Password", type="password")

    if st.button("🔓 Decrypt"):
        if uploaded_file and password:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            decrypted_msg = decrypt_image(img, password)  # Updated function with password
            if decrypted_msg:
                st.success(f"✅ Decrypted Message: {decrypted_msg}")
            else:
                st.error("❌ Incorrect Password! Unable to decrypt the message.")

        else:
            st.error("⚠ Please upload the encrypted image and enter the correct password.")
