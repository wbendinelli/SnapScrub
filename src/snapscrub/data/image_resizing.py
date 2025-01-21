import os
import logging
from PIL import Image

def resize_images(folder_path, output_path, size=(256, 256)):
    """
    Resize images in a folder to the specified size and save them to the output folder.

    Parameters:
        folder_path (str): Path to the folder containing images to resize.
        output_path (str): Path to the folder to save resized images.
        size (tuple): Desired size for the resized images (width, height).

    Returns:
        list: List of resized image filenames.
    """
    if not os.path.exists(folder_path):
        logging.error(f"Source folder not found: {folder_path}")
        return []

    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    resized_files = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        output_file_path = os.path.join(output_path, file_name)

        try:
            with Image.open(file_path) as img:
                img_resized = img.resize(size)
                img_resized.save(output_file_path)
                resized_files.append(file_name)
                logging.info(f"Resized: {file_name}")
        except Exception as e:
            logging.error(f"Error resizing {file_name}: {e}")

    logging.info(f"Total images resized: {len(resized_files)}")
    return resized_files