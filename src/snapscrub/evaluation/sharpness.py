import logging
import cv2

def calculate_sharpness(image_path):
    """
    Calculate the sharpness of an image using the Laplacian variance.

    Parameters:
        image_path (str): Path to the image.

    Returns:
        float: Sharpness score (higher is sharper).
    """
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            logging.error(f"Image not found: {image_path}")
            return 0.0
        return cv2.Laplacian(image, cv2.CV_64F).var()
    except Exception as e:
        logging.error(f"Error calculating sharpness: {e}")
        return 0.0