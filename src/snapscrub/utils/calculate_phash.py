import logging
from PIL import Image
import imagehash

def calculate_phash(image_path):
    """
    Calculate the perceptual hash (pHash) of an image.

    Parameters:
        image_path (str): Path to the image.

    Returns:
        str: The perceptual hash value.
    """
    try:
        img = Image.open(image_path)
        phash = imagehash.phash(img)
        return str(phash)
    except Exception as e:
        logging.error(f"Error calculating pHash for {image_path}: {e}")
        return None