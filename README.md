# **StegaCrypt: Secure Image-Based Steganography Using OpenCV & Streamlit** 🚀🔐  

## **Overview**  
**StegaCrypt** is an interactive image steganography application that allows users to securely hide and retrieve messages within images. Built using OpenCV, NumPy, and Streamlit, this tool ensures seamless encryption and decryption while maintaining the image’s visual integrity. 
The Image Steganography App uses a Least Significant Bit (LSB) Modification Technique for encoding and decoding hidden messages within images. Below is a breakdown of how the encryption and decryption process works:

### **🔐 Encryption Steps:**  
- Convert each character of the message to its **ASCII value**.  
- Embed the ASCII values into the **RGB pixel values** of the image.  
- Traverse the image in a cyclic order across **R, G, and B channels**.  
- Append a **null character (`\0`)** to mark the end of the message.  
- Save the modified image as the **encrypted image**.  

### **🔓 Decryption Steps:**  
- Read pixel values in the same order as encryption.  
- Convert the extracted values back to **characters** using ASCII mapping.  
- Stop reading when the **null character (`\0`)** is found.  
- Display the **decoded secret message**. 🚀


## **✨ Features**  

🔒 **Secure Message Encryption** – Hide secret messages inside images without altering their appearance.  

🖼️ **Seamless Image Processing** – Uses OpenCV and NumPy to efficiently encode and decode messages.  

⚡ **Lightning-Fast Encryption & Decryption** – Instantly embed and retrieve messages.  

🎨 **User-Friendly Interface** – A simple and interactive UI powered by Streamlit.  

📤 **Easy File Handling** – Upload, encrypt, download, and decrypt images effortlessly.  

📌 **No Data Loss** – Ensures accurate extraction of hidden messages without corruption.  

🛠️ **Lightweight & Portable** – Runs smoothly on any system with minimal dependencies.  

🔑 **Password Protection (Future Enhancement)** – Adds an extra security layer for hidden messages.  

## **🛠 Requirements**  
Before running **StegaCrypt**, ensure you have the following installed:  
- Python 3.x  
- OpenCV (`opencv-python`)  
- NumPy (`numpy`)  
- Streamlit (`streamlit`)  

## **📥 Installation**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/StegaCrypt.git
   cd StegaCrypt
