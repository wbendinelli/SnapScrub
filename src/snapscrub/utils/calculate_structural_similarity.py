import cv2
import logging
from skimage.metrics import structural_similarity as ssim

def calculate_structural_similarity(image1_path, image2_path):
    """
    Calculate the Structural Similarity Index (SSIM) between two images.

    Parameters:
        image1_path (str): Path to the first image.
        image2_path (str): Path to the second image.

    Returns:
        float: SSIM similarity score (0 to 1).
    """
    try:
        img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

        if img1 is None or img2 is None:
            return 0.0

        img1 = cv2.resize(img1, (256, 256))
        img2 = cv2.resize(img2, (256, 256))

        score, _ = ssim(img1, img2, full=True)
        return score
    except Exception as e:
        logging.error(f"Error calculating SSIM: {e}")
        return 0.0