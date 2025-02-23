import cv2
import numpy as np
import base64
from cryptography.fernet import Fernet

# Generate a key from password
def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32).encode()[:32])

# Decrypt message with AES
def decrypt_message(encrypted_message, password):
    try:
        key = generate_key(password)
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_message.encode()).decode()  # Return decrypted text
    except:
        return "Wrong password"

# Define value-to-character mapping for image decoding
c = {i: chr(i) for i in range(255)}

def decrypt_image(image, password):
    encrypted_msg = ""
    m, n, z = 0, 0, 0

    while True:
        char = c.get(image[n, m, z], "")
        if char == "\0":
            break
        encrypted_msg += char
        n = (n + 1) % image.shape[0]
        m = (m + 1) % image.shape[1]
        z = (z + 1) % 3

    return decrypt_message(encrypted_msg, password)  # Decrypt message
