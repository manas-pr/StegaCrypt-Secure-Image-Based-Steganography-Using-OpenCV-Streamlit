import numpy as np
import cv2

def decrypt_image(image, password=None):
    """Decrypts a message from an image, verifying password if provided."""
    decrypted_msg = ""
    m, n, z = 0, 0, 0

    while True:
        char = chr(image[n, m, z])  # Convert pixel value back to character
        if char == "\0":  # End of message
            break
        decrypted_msg += char
        n = (n + 1) % image.shape[0]
        m = (m + 1) % image.shape[1]
        z = (z + 1) % 3

    # Verify password if provided
    if password:
        if decrypted_msg.startswith(password):
            return decrypted_msg[len(password):]  # Return message without password
        else:
            return "❌ Incorrect password!"

    return decrypted_msg

