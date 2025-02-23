import cv2
import numpy as np
import base64
from Crypto.Cipher import AES
from hashlib import sha256

# Padding function for AES encryption
def pad_message(message):
    return message + (16 - len(message) % 16) * chr(16 - len(message) % 16)

# AES encryption function
def encrypt_message(message, password):
    key = sha256(password.encode()).digest()  # Generate AES key from password
    cipher = AES.new(key, AES.MODE_ECB)  # Using ECB mode
    encrypted_bytes = cipher.encrypt(pad_message(message).encode())  # Encrypt
    return base64.b64encode(encrypted_bytes).decode()  # Encode in base64

# Function to embed message into an image
def encrypt_image(image, message, password):
    img = image.copy()
    
    # Encrypt the message
    encrypted_message = encrypt_message(message, password)
    message_length = len(encrypted_message)

    # Store message length in the first 8 pixels
    for i in range(8):
        img[i, 0, 0] = (message_length >> (i * 8)) & 255  # Store length in red channel

    # Embed message characters in the image
    m, n, z = 8, 0, 0  # Start from pixel index 8 to avoid overwriting length
    for char in encrypted_message:
        img[n, m, z] = ord(char)  # Store ASCII value of character
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return img
