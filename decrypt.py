import cv2

def decrypt_message(image_path, length):
    img = cv2.imread(image_path)

    if img is None:
        raise FileNotFoundError("Image not found. Check the path.")

    c = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    message = ""

    for _ in range(length):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return message
