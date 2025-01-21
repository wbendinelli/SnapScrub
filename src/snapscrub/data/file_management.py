import os
import shutil
import logging

def transfer_images(source_folder, destination_folder):
    """
    Transfer image files from the source folder to the destination folder.

    Parameters:
        source_folder (str): The directory containing original images.
        destination_folder (str): The directory to store transferred images.

    Returns:
        list: List of successfully transferred files.
    """
    if not os.path.exists(source_folder):
        logging.error(f"Source folder not found: {source_folder}")
        return []

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder, exist_ok=True)

    transferred_files = []
    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        if os.path.isfile(source_path):
            try:
                shutil.copy2(source_path, destination_path)
                transferred_files.append(file_name)
                logging.info(f"Transferred: {file_name}")
            except Exception as e:
                logging.error(f"Error transferring {file_name}: {e}")

    logging.info(f"Total files transferred: {len(transferred_files)}")
    return transferred_files