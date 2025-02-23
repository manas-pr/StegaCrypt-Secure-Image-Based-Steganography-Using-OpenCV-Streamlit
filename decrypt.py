import cv2
import numpy as np
import base64
from Crypto.Cipher import AES
from hashlib import sha256

import base64
from Crypto.Cipher import AES
import hashlib

def decrypt_message(encrypted_message, password):
    try:
        key = hashlib.sha256(password.encode()).digest()
        encrypted_data = base64.b64decode(encrypted_message)  # Ensure correct decoding

        nonce = encrypted_data[:16]
        tag = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]

        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted_bytes = cipher.decrypt_and_verify(ciphertext, tag)
        
        return decrypted_bytes.decode()
    
    except (ValueError, KeyError, base64.binascii.Error):
        return None  # Handle incorrect decryption or base64 errors


# Function to extract message from image
def decrypt_image(image, password):
    encrypted_message = ""
    m, n, z = 0, 0, 0

    while True:
        char = chr(image[n, m, z])  # Retrieve ASCII values
        if char == "\0":  # Stop at termination
            break
        encrypted_message += char
        n = (n + 1) % image.shape[0]
        m = (m + 1) % image.shape[1]
        z = (z + 1) % 3

    return decrypt_message(encrypted_message, password)

