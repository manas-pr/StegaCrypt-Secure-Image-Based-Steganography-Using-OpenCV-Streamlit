import cv2
import numpy as np
import streamlit as st
import os
import tempfile
from encrypt import encrypt_image  # Import encryption function
from decrypt import decrypt_image  # Import decryption function


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
    text-align: left;
}

/* Set specific labels and sidebar header to white */
div[data-testid="stFileUploader"] label,
div[data-testid="stTextInput"] label,
div[data-testid="stTextArea"] label {
    color: white !important;
    font-weight: bold;
}

/* Make the sidebar header white and align it to the left */
section[data-testid="stSidebar"] h1 {
    color: white !important;
    text-align: left !important;
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
🎓 *Electronics and Communication Engineering (MTech/MS)*  

🤖 **Focus Areas:**  
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
    st.markdown("<h2>🔐 Encrypt a Message into an Image</h2>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "png"])
    message = st.text_area("📝 Enter Secret Message")
    password = st.text_input("🔑 Set a Password (Optional)", type="password")

    if st.button("🔐 Encrypt & Save"):
        if uploaded_file and message:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            encrypted_img = encrypt_image(img, message, password if password else None)

            # Save in a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                encrypted_path = temp_file.name
                cv2.imwrite(encrypted_path, encrypted_img)

            st.image(encrypted_path, caption="🔒 Encrypted Image", use_column_width=True)
            st.success("✅ Message Encrypted! Download the encrypted image below.")

            with open(encrypted_path, "rb") as f:
                st.download_button("📥 Download Encrypted Image", f, file_name="encryptedImage.png", mime="image/png")

        else:
            st.error("⚠ Please upload an image and enter a message.")

# Decryption Section
elif option == "Decrypt Message":
    st.markdown("<h2>🔓 Decrypt a Message from an Image</h2>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("📥 Upload Encrypted Image", type=["png", "jpg"])  
    password = st.text_input("🔑 Enter Password (If Required)", type="password")

    if st.button("🔓 Decrypt"):
        if uploaded_file:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

            decrypted_msg = decrypt_image(img, password if password else None)
            st.success(f"✅ Decrypted Message: {decrypted_msg}")

        else:
            st.error("⚠ Please upload the encrypted image and enter the correct password if required.")
