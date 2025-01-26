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
        None
    """
    logging.info("Starting resizing process...")

    # Clear the output folder before resizing
    if os.path.exists(output_path):
        for file_name in os.listdir(output_path):
            file_path = os.path.join(output_path, file_name)
            try:
                os.remove(file_path)
            except Exception as e:
                logging.error(f"Failed to delete {file_name}: {e}")
    else:
        os.makedirs(output_path, exist_ok=True)

    files = os.listdir(folder_path)
    if not files:
        logging.warning("No files found to resize. Please check the path.")
        return

    resized_count = 0
    failed_count = 0

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        try:
            img = Image.open(file_path)
            img_resized = img.resize(size)
            img_resized.save(os.path.join(output_path, file_name))

            logging.info(f"Resized: {file_name}")
            resized_count += 1
        except Exception as e:
            logging.error(f"Error resizing image {file_name}: {e}")
            failed_count += 1

    logging.info(f"Resizing process completed: {resized_count} files resized, {failed_count} files failed.")