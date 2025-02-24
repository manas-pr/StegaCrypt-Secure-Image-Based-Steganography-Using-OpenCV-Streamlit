import cv2
import numpy as np

def encrypt_image(image, message, password=None):
    """Encrypts a message into an image using LSB steganography with optional password protection."""
    
    # Combine password with the message if provided
    if password:
        message = password + ":" + message  # Store password as a prefix
    message += "#####"

    # Convert message into binary format
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    data_index = 0
    binary_message_length = len(binary_message)

    # Embed binary message into image
    for row in image:
        for pixel in row:
            for i in range(3):  # Iterate over RGB channels
                if data_index < binary_message_length:
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
                else:
                    return image  # Stop modifying once the message is embedded
    return image
