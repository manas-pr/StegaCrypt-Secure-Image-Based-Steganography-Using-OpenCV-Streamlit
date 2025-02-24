import cv2
import numpy as np

def decrypt_image(image, password=None):
    """Decrypts a hidden message from an image and checks for password protection."""

    binary_message = ""
    for row in image:
        for pixel in row:
            for i in range(3):  # Extract LSB from RGB channels
                binary_message += str(pixel[i] & 1)

    # Convert binary to string
    message_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    extracted_message = "".join([chr(int(byte, 2)) for byte in message_bytes])

    # Ensure the delimiter exists
    if "#####" not in extracted_message:
        return "Error: No hidden message found."

    extracted_message = extracted_message.split("#####")[0]  # Remove delimiter

    # If a password was used, validate it
    if ":" in extracted_message:
        stored_password, actual_message = extracted_message.split(":", 1)
        if password:
            if stored_password == password:
                return actual_message  # Return decrypted message
            else:
                return "❌ Incorrect password!"
        else:
            return "❌ This message is password protected. Please provide a password."

    return extracted_message  # Return message if no password was set
