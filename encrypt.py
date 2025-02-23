import cv2
import numpy as np
import hashlib
from Crypto.Cipher import AES
import base64

def encrypt_image(image, message, password):
    # Hash the password
    password_hash = hashlib.sha256(password.encode()).digest()
    
    # Pad the message to be AES block-size compatible
    def pad(text):
        return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)
    
    padded_message = pad(message)

    # Encrypt message using AES
    cipher = AES.new(password_hash, AES.MODE_ECB)
    encrypted_msg = base64.b64encode(cipher.encrypt(padded_message.encode())).decode()

    img = image.copy()
    m, n, z = 0, 0, 0

    for char in encrypted_msg:
        img[n, m, z] = ord(char)
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return img
