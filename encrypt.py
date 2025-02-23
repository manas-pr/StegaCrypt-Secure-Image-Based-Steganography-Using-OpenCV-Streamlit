import cv2
import numpy as np
import base64
from cryptography.fernet import Fernet

# Generate a key from password
def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32).encode()[:32])

# Encrypt message with AES
def encrypt_message(message, password):
    key = generate_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(message.encode()).decode()  # Return encrypted text

# Define character-to-value mapping for image encoding
d = {chr(i): i for i in range(255)}

def encrypt_image(image, message, password):
    encrypted_msg = encrypt_message(message, password)  # Encrypt message
    encrypted_msg += "\0"  # Add termination character
    img = image.copy()
    m, n, z = 0, 0, 0

    for char in encrypted_msg:
        img[n, m, z] = d.get(char, 0)  # Store encrypted message
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return img
