import cv2
import numpy as np

# Define the dictionary mapping pixel values to characters
c = {i: chr(i) for i in range(256)}  # Maps 0-255 to ASCII characters

def decrypt_image(image):
    decrypted_msg = ""
    m, n, z = 0, 0, 0

    while True:
        char = c.get(image[n, m, z], "")
        if char == "\0":  # Stop at termination character
            break
        decrypted_msg += char
        n = (n + 1) % image.shape[0]
        m = (m + 1) % image.shape[1]
        z = (z + 1) % 3

    return decrypted_msg
