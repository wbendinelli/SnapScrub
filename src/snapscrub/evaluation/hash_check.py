import logging
import hashlib
from PIL import Image
import numpy as np

def calculate_hash(image_path):
    """
    Calculate the perceptual hash of an image for duplicate detection.

    Parameters:
        image_path (str): Path to the image.

    Returns:
        str: Hexadecimal hash of the image.
    """
    try:
        with Image.open(image_path) as img:
            img = img.convert("L").resize((8, 8), Image.ANTIALIAS)
            pixels = np.array(img)
            avg = pixels.mean()
            hash_str = "".join(['1' if pixel > avg else '0' for pixel in pixels.flatten()])
            return hashlib.md5(hash_str.encode()).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for {image_path}: {e}")
        return None