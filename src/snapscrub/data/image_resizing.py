import os
import logging
from PIL import Image, UnidentifiedImageError

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

    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff'))]
    if not files:
        logging.warning("No files found to resize. Please check the path.")
        return

    resized_count = 0
    failed_count = 0

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        output_file_path = os.path.join(output_path, file_name)

        try:
            with Image.open(file_path) as img:
                img.verify()  # Verifica se a imagem não está corrompida

            # Reabrir após a verificação para evitar erros ao redimensionar
            with Image.open(file_path) as img:
                img = img.convert("RGB")
                img_resized = img.resize(size, Image.Resampling.LANCZOS)
                img_resized.save(output_file_path, quality=90)

            logging.info(f"Resized and saved: {output_file_path}")
            resized_count += 1

        except UnidentifiedImageError:
            logging.error(f"Unidentified or corrupt image: {file_name}")
            failed_count += 1
        except Exception as e:
            logging.error(f"Error processing {file_name}: {e}")
            failed_count += 1

    logging.info(f"Resizing process completed: {resized_count} files resized, {failed_count} files failed.")