import logging
import cv2
from skimage.metrics import structural_similarity as ssim

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
            logging.error(f"One or both images not found: {image1_path}, {image2_path}")
            return 0.0
        image1 = cv2.resize(image1, (256, 256))
        image2 = cv2.resize(image2, (256, 256))
        score, _ = ssim(image1, image2, full=True)
        return score
    except Exception as e:
        logging.error(f"Error calculating similarity: {e}")
        return 0.0