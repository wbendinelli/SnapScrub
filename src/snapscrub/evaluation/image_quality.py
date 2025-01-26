import cv2
import logging
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import os

def calculate_similarity(image1_path, image2_path):
    """
    Calculate the Structural Similarity Index (SSIM) between two images.

    Parameters:
        image1_path (str): Path to the first image.
        image2_path (str): Path to the second image.

    Returns:
        float: SSIM similarity score (0 to 1).
    """
    try:
        image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
        image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
        if image1 is None or image2 is None:
            return 0.0
        image1 = cv2.resize(image1, (256, 256))
        image2 = cv2.resize(image2, (256, 256))
        score, _ = ssim(image1, image2, full=True)
        return score
    except Exception as e:
        logging.error(f"Error calculating similarity: {e}")
        return 0.0

def calculate_sharpness(image_path):
    """
    Calculate the sharpness of an image using the Laplacian variance.

    Parameters:
        image_path (str): Path to the image.

    Returns:
        float: Sharpness score (higher is sharper).
    """
    if not os.path.exists(image_path):
        logging.error(f"Image not found: {image_path}")
        return 0.0

    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            logging.error(f"Unable to read the image: {image_path}")
            return 0.0
        return cv2.Laplacian(image, cv2.CV_64F).var()
    except Exception as e:
        logging.error(f"Error calculating sharpness for {image_path}: {e}")
        return 0.0

def calculate_exposure(image_path):
    """
    Calculate the average brightness of an image.

    Parameters:
        image_path (str): Path to the image.

    Returns:
        float: Exposure score (0 to 1, where 0.5 is ideal exposure).
    """
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            return 0.0
        return image.mean() / 255.0
    except Exception as e:
        logging.error(f"Error calculating exposure: {e}")
        return 0.0