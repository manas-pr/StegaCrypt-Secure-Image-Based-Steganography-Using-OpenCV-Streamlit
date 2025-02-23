import cv2
import os

def encrypt_message(image_path, message, output_path="encryptedImage.jpg"):
    img = cv2.imread(image_path)

    if img is None:
        raise FileNotFoundError("Image not found. Check the path.")

    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = d[char]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    cv2.imwrite(output_path, img)
    return output_path
