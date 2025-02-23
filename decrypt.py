import cv2
import numpy as np
import base64
from Crypto.Cipher import AES
from hashlib import sha256

# AES decryption function
def decrypt_message(encrypted_message, password):
    key = sha256(password.encode()).digest()  # Generate AES key
    cipher = AES.new(key, AES.MODE_ECB)  # Using ECB mode
    decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_message))  # Decrypt
    return decrypted_bytes.decode().rstrip(chr(decrypted_bytes[-1]))  # Remove padding

# Function to extract message from image
def decrypt_image(image, password):
    decrypted_msg = ""

    # Extract message length from first 8 pixels
    message_length = 0
    for i in range(8):
        message_length |= image[i, 0, 0] << (i * 8)

    m, n, z = 8, 0, 0  # Start reading after length storage
    encrypted_msg = ""
    
    for _ in range(message_length):
        encrypted_msg += chr(image[n, m, z])  # Read ASCII values
        n = (n + 1) % image.shape[0]
        m = (m + 1) % image.shape[1]
        z = (z + 1) % 3

    # Decrypt the message
    return decrypt_message(encrypted_msg, password)
