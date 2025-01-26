import os
import logging
import shutil
from PIL import Image
import pillow_heif

def heic_to_rgb(image_path, output_path, target_format='jpeg'):
    """
    Convert a HEIC image to the specified format using pillow-heif.

    Parameters:
        image_path (str): Path to the HEIC image.
        output_path (str): Path to save the converted image.
        target_format (str): Format to convert to (default: 'jpeg').
    """
    try:
        heif_image = pillow_heif.open_heif(image_path)
        image = Image.frombytes(
            heif_image.mode,
            heif_image.size,
            heif_image.data,
            "raw",
            heif_image.mode,
            heif_image.stride,
        )
        image.convert("RGB").save(output_path, format=target_format.upper())
        logging.info(f"Successfully converted {image_path} to {target_format.upper()}")
    except Exception as e:
        logging.error(f"Failed to convert {image_path}: {e}")
        raise

def process_images(source_folder, destination_folder, target_format='jpeg'):
    """
    Process images from a source folder and copy them to a destination folder.

    Parameters:
        source_folder (str): Folder containing the source images.
        destination_folder (str): Folder where processed images will be saved.
        target_format (str): Target format for image conversion (default: 'jpeg').

    Returns:
        None
    """
    try:
        # Ensure the source folder exists
        if not os.path.exists(source_folder):
            logging.error(f"Source folder '{source_folder}' does not exist.")
            return

        # Ensure the destination folder is clean
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder, exist_ok=True)
        else:
            for file_name in os.listdir(destination_folder):
                file_path = os.path.join(destination_folder, file_name)
                try:
                    os.remove(file_path)
                except Exception as e:
                    logging.warning(f"Failed to delete file {file_name}: {e}")

        # Ensure the converted folder exists inside the destination folder
        converted_folder = os.path.join(destination_folder, "converted")
        os.makedirs(converted_folder, exist_ok=True)

        # Initialize counters
        copied_count = 0
        converted_count = 0
        skipped_count = 0

        # Process files in the source folder
        for file_name in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, f"{os.path.splitext(file_name)[0]}.{target_format}")

            if not os.path.isfile(source_path):
                logging.warning(f"Skipping non-file entry: {file_name}")
                continue

            try:
                if file_name.lower().endswith('.heic'):
                    heic_to_rgb(source_path, destination_path, target_format)
                    shutil.move(destination_path, os.path.join(converted_folder, os.path.basename(destination_path)))
                    converted_count += 1
                else:
                    with Image.open(source_path) as img:
                        img.convert("RGB").save(destination_path, format=target_format.upper())
                    copied_count += 1
            except Exception as e:
                logging.warning(f"Skipped file {file_name} due to error: {e}")
                skipped_count += 1

        # Log summary
        logging.info(f"Summary of image processing:")
        logging.info(f" - Copied without conversion: {copied_count}")
        logging.info(f" - Converted from HEIC to {target_format.upper()}: {converted_count}")
        logging.info(f" - Skipped files (not processed): {skipped_count}")

    except Exception as e:
        logging.error(f"An error occurred during image processing: {e}")