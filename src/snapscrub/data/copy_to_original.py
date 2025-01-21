import os
import shutil
import logging

def copy_to_original(source_path, target_path):
    """
    Copy files from a source directory to the 'original' folder.

    This function copies all files from the source directory to the 'original' folder
    created by the `create_folders` function. Existing files in the target folder will
    be replaced.

    Parameters:
        source_path (str): The directory containing files to be copied.
        target_path (str): The destination 'original' folder.

    Returns:
        list: A list of file names successfully copied.
    """
    if not os.path.exists(source_path):
        logging.error(f"Source path does not exist: {source_path}")
        return []

    if not os.path.exists(target_path):
        logging.error(f"Target path does not exist: {target_path}")
        return []

    copied_files = []
    errors = []

    for file_name in os.listdir(source_path):
        source_file = os.path.join(source_path, file_name)
        target_file = os.path.join(target_path, file_name)

        # Only copy files, skip directories
        if os.path.isfile(source_file):
            try:
                shutil.copy2(source_file, target_file)
                copied_files.append(file_name)
            except Exception as e:
                errors.append((file_name, str(e)))

    logging.info(f"Copied files: {copied_files}")
    if errors:
        logging.error(f"Errors during copy: {errors}")

    return copied_files