import cv2
import logging

def calculate_hash(image_path):
    """
    Calculate a perceptual hash (dHash) for an image.

    Parameters:
        image_path (str): Path to the image file.

    Returns:
        str: A hash value representing the image.
    """
    try:
        # Load the image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError("Image not found or unable to read.")

        # Resize to 9x8 to calculate differences
        resized = cv2.resize(image, (9, 8), interpolation=cv2.INTER_AREA)

        # Compute the differences between adjacent pixels
        diff = resized[:, 1:] > resized[:, :-1]

        # Convert differences to a hash value
        hash_val = ''.join(str(int(x)) for x in diff.flatten())
        return hash_val
    except Exception as e:
        logging.error(f"Error calculating hash for {image_path}: {e}")
        return None