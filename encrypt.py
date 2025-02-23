import cv2
import numpy as np
import streamlit as st
import os

# Define character-to-value mapping
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

def encrypt_image(image, message):
    img = image.copy()
    message += "\0"  # Add termination character
    m, n, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return img
