import cv2
import numpy as np
import streamlit as st
import os
from encrypt import encrypt_image  # Import encryption function
from decrypt import decrypt_image  # Import decryption function


# Set background image using CSS
# Set background image and text styling using CSS
page_bg_img = """
<style>
.stApp {
    background-image: url("https://developer-blogs.nvidia.com/wp-content/uploads/2023/06/deep-learning-visual.png");
    background-size: cover;
    background-attachment: fixed;
}

/* Set title font color to white */
h1 {
    color: white !important;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit UI
st.markdown("<h1 style='text-align: center; color: white;'>🔒 StegaCrypt - Secure Image Steganography App</h1>", unsafe_allow_html=True)


# Sidebar options
st.sidebar.header("📌 Navigation")
option = st.sidebar.radio("Choose an option:", ("Encrypt Message", "Decrypt Message"))

# About section in the sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 About the Developer")
st.sidebar.markdown("""
**Manas Pratim Das**  
🎓 *Electronics and Communication Engineering (MTech/MS)*  

🤖 **Focus Areas:**  
       ✅ Artificial Intelligence & Machine Learning  
       ✅ Deep Learning & Secure Computing  
       ✅ Neuromorphic Computing  

📌 **Connect with Me:**  
🔗 [LinkedIn](https://www.linkedin.com/in/manas-pratim-das-b95200197/)     
🐙 [GitHub](https://github.com/manaspr94)     
📧 [Email](mailto:manas.pr94@gmail.com)     
  
""")  







# Encryption Section
if option == "Encrypt Message":
    st.markdown("<h2 style='color: white;'>Encrypt a Message into an Image</h2>", unsafe_allow_html=True)
    
    st.markdown("<p style='color: white;'>📤 Upload an Image</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["jpg", "png"])
    
    st.markdown("<p style='color: white;'>📝 Enter Secret Message</p>", unsafe_allow_html=True)
    message = st.text_area("", key="message")
    
    st.markdown("<p style='color: white;'>🔑 Set a Password (Optional)</p>", unsafe_allow_html=True)
    password = st.text_input("", type="password", key="password")


    if st.button("🔐 Encrypt & Save"):
        if uploaded_file and message:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            encrypted_img = encrypt_image(img, message, password if password else None)
            cv2.imwrite("encryptedImage.png", encrypted_img)
            st.image("encryptedImage.png", caption="🔒 Encrypted Image", use_column_width=True)
            st.success("✅ Message Encrypted! Download the encrypted image below.")

            with open("encryptedImage.png", "rb") as f:
                st.download_button("📥 Download Encrypted Image", f, file_name="encryptedImage.png", mime="image/png")

        else:
            st.error("⚠ Please upload an image and enter a message.")

# Decryption Section
elif option == "Decrypt Message":
    st.markdown("<h2 style='color: white;'>Decrypt a Message from an Image</h2>", unsafe_allow_html=True)
    
    st.markdown("<p style='color: white;'>📥 Upload Encrypted Image</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["png", "jpg"], key="decrypt_file")
    
    st.markdown("<p style='color: white;'>🔑 Enter Password (If Required)</p>", unsafe_allow_html=True)
    password = st.text_input("", type="password", key="decrypt_password")


    if st.button("🔓 Decrypt"):
        if uploaded_file:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            decrypted_msg = decrypt_image(img, password if password else None)
            st.success(f"✅ Decrypted Message: {decrypted_msg}")

        else:
            st.error("⚠ Please upload the encrypted image and enter the correct password if required.")
