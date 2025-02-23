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


# Function to XOR encrypt/decrypt a message using a password
def xor_encrypt_decrypt(message, password):
    return ''.join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(message))


# Function to convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)


# Function to convert binary to text
def binary_to_text(binary_data):
    message_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(byte, 2)) for byte in message_bytes)


# Function to encrypt a message into an image
def encrypt_image(image, message, password):
    message = xor_encrypt_decrypt(message, password) + "#####"  # Add delimiter
    binary_message = text_to_binary(message)
    
    max_bytes = image.shape[0] * image.shape[1] * 3  # Total number of bytes in the image
    if len(binary_message) > max_bytes:
        raise ValueError("Error: Message too large to hide in this image! Use a larger image.")
    
    data_index = 0
    binary_message_length = len(binary_message)

    for row in image:
        for pixel in row:
            for i in range(3):  # Iterate over RGB channels
                if data_index < binary_message_length:
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])  # Modify LSB
                    data_index += 1
                else:
                    break
    return image



# Function to decrypt a message from an image
def decrypt_image(image, password):
    binary_message = ""

    for row in image:
        for pixel in row:
            for i in range(3):  # Extract LSB from RGB channels
                binary_message += str(pixel[i] & 1)

    extracted_message = binary_to_text(binary_message)

    if "#####" in extracted_message:
        decrypted_msg = extracted_message.split("#####")[0]
        return xor_encrypt_decrypt(decrypted_msg, password)  # Decrypt using the same password
    else:
        return "Error: No hidden message found."


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
📧 [Email](mailto:manas.pr94@gmail.com)  
🐙 [GitHub](https://github.com/manas-pr)  
""", unsafe_allow_html=True)


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

            encrypted_img = encrypt_image(img, message, password)
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

            decrypted_msg = decrypt_image(img, password)

            if "Error" in decrypted_msg:
                st.error("❌ Incorrect password or no hidden message found!")
            else:
                st.success(f"✅ Decrypted Message: {decrypted_msg}")

        else:
            st.error("⚠ Please upload the encrypted image and enter the correct password.")
