import cv2
import logging

def calculate_histogram_similarity(image1_path, image2_path):
    """
    Calculate histogram similarity between two images using correlation.

    Parameters:
        image1_path (str): Path to the first image.
        image2_path (str): Path to the second image.

    Returns:
        float: Similarity score (1.0 = identical, 0.0 = completely different).
    """
    try:
        img1 = cv2.imread(image1_path)
        img2 = cv2.imread(image2_path)

        if img1 is None or img2 is None:
            return 0.0

        hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

        cv2.normalize(hist1, hist1)
        cv2.normalize(hist2, hist2)

        similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
        return similarity
    except Exception as e:
        logging.error(f"Error calculating histogram similarity: {e}")
        return 0.0