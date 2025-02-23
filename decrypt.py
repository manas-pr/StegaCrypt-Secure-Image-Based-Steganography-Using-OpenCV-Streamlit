import cv2
import numpy as np
import cv2
import numpy as np
import streamlit as st
import os
# Define dictionary mapping pixel values to ASCII characters
c = {i: chr(i) for i in range(256)}  

def decrypt_image(image):
    decrypted_msg = ""
    m, n, z = 0, 0, 0
    height, width, _ = image.shape  # Get image dimensions

    while True:
        pixel_value = image[n, m, z]
        char = c.get(pixel_value, "")

        if char == "\0":  # Stop if termination character found
            break
        
        decrypted_msg += char

        # Move to next pixel in a structured way
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == width:
                m = 0
                n += 1
                if n == height:  # Stop at end of image
                    break

    return decrypted_msg
