import numpy as np
import cv2

def encrypt_image(image, message, password=None):
    """Encrypts a message into an image using pixel manipulation."""
    if password:
        message = password + message  # Simple way to integrate password
    message += "\0"  # End-of-message marker

    img = image.copy()
    m, n, z = 0, 0, 0

    for char in message:
        img[n, m, z] = ord(char)  # Convert character to ASCII value
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return img
