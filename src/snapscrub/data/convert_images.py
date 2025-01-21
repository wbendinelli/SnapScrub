import os
import logging
from PIL import Image
import pillow_heif
import shutil
import subprocess

def convert_heic_to_jpeg(input_path, output_path):
    """
    Convert a HEIC image to JPEG using multiple approaches (pillow-heif, sips).

    Parameters:
        input_path (str): Path to the HEIC image.
        output_path (str): Path to save the converted image.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        heif_image = pillow_heif.open_heif(input_path)
        image = Image.frombytes(
            heif_image.mode,
            heif_image.size,
            heif_image.data,
            "raw",
            heif_image.mode,
            heif_image.stride,
        )
        image.convert("RGB").save(output_path, format="JPEG")
        logging.info(f"Successfully converted {input_path} using pillow-heif.")
        return True
    except Exception as e:
        logging.warning(f"pillow-heif failed for {input_path}, error: {e}")

    try:
        # Using macOS sips command as a fallback
        command = f"sips -s format jpeg '{input_path}' --out '{output_path}'"
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            logging.info(f"Successfully converted {input_path} using sips.")
            return True
    except Exception as e:
        logging.warning(f"sips failed for {input_path}, error: {e}")

    logging.error(f"Failed to convert HEIC file: {input_path}")
    return False


def process_all_images(source_folder, destination_folder):
    """
    Process all images in the source folder by converting HEIC to JPEG 
    and copying other image formats directly.

    Parameters:
        source_folder (str): Folder containing original images.
        destination_folder (str): Folder where processed images will be saved.

    Returns:
        dict: Summary containing counts of processed and copied images.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.heic')
    all_files = [f for f in os.listdir(source_folder) if f.lower().endswith(image_extensions)]

    if not all_files:
        logging.warning(f"No images found in {source_folder}")
        return {"converted": 0, "copied": 0, "errors": 0}

    converted_count = 0
    copied_count = 0
    error_count = 0

    for file_name in all_files:
        input_path = os.path.join(source_folder, file_name)
        output_path = os.path.join(destination_folder, f"{os.path.splitext(file_name)[0]}.jpg")

        if file_name.lower().endswith('.heic'):
            if convert_heic_to_jpeg(input_path, output_path):
                converted_count += 1
            else:
                error_count += 1
        else:
            # Copy other formats directly
            try:
                shutil.copy2(input_path, os.path.join(destination_folder, file_name))
                copied_count += 1
                logging.info(f"Copied {file_name} to {destination_folder}")
            except Exception as e:
                logging.error(f"Failed to copy {file_name}: {e}")
                error_count += 1

    logging.info(f"Processing completed: {converted_count} HEIC converted, {copied_count} images copied, {error_count} errors.")
    return {"converted": converted_count, "copied": copied_count, "errors": error_count}