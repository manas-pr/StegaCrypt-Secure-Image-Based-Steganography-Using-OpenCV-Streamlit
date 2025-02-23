import cv2
import numpy as np
import hashlib
from Crypto.Cipher import AES
import base64

def decrypt_image(image, password):
    # Hash the password (must match the encryption process)
    password_hash = hashlib.sha256(password.encode()).digest()
    
    extracted_msg = ""
    m, n, z = 0, 0, 0

    while True:
        char = chr(image[n, m, z])
        if char == '\x00':  # Stop if null character found (end of message)
            break
        extracted_msg += char
        n = (n + 1) % image.shape[0]
        m = (m + 1) % image.shape[1]
        z = (z + 1) % 3

    try:
        # Decrypt message
        cipher = AES.new(password_hash, AES.MODE_ECB)
        decrypted_msg = cipher.decrypt(base64.b64decode(extracted_msg)).decode()

        # Remove padding
        def unpad(text):
            return text[:-ord(text[-1])]

        return unpad(decrypted_msg)
    
    except Exception:
        return "❌ Incorrect Password!"
