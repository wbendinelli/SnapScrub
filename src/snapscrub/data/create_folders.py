import os
import shutil
import logging

def create_folders(root_path):
    """
    Create the necessary directory structure for the image classification pipeline.

    This function ensures the following subdirectories are created under the specified root path:
    - `original`: Contains the original images before any processing.
    - `resized`: Contains resized images for analysis.
    - `converted`: Contains images converted to a standard format.
    - `cleaned`: Contains cleaned images (without duplicates or corrupt files).
    - `results`: Stores results such as evaluation tables or reports.

    Parameters:
        root_path (str): The root directory where the subdirectories will be created.

    Returns:
        dict: A dictionary containing the names of the subdirectories as keys and their full paths as values.
    """
    folders = {
        "original": os.path.join(root_path, "original"),
        "resized": os.path.join(root_path, "resized"),
        "converted": os.path.join(root_path, "converted"),
        "cleaned": os.path.join(root_path, "cleaned"),
        "results": os.path.join(root_path, "results"),
    }

    # Remove existing directories
    for folder in folders.values():
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder, exist_ok=True)

    logging.info(f"Project initialized with folders: {list(folders.values())}")
    return folders