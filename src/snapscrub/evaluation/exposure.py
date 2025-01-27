import logging
import cv2
import numpy as np

def calculate_exposure(image_path):
    """
    Calculate the exposure level of an image using average brightness.

    Parameters:
        image_path (str): Path to the image.

    Returns:
        float: Exposure level (higher means brighter).
    """
    try:
        image = cv2.imread(image_path)
        if image is None:
            logging.error(f"Image not found: {image_path}")
            return 0.0
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return np.mean(gray)
    except Exception as e:
        logging.error(f"Error calculating exposure: {e}")
        return 0.0