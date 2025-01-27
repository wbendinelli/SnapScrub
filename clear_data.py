import os
import shutil
import logging

def clear_data(root_path):
    """
    Delete all contents of the 'data' directory to reset the pipeline environment.

    Parameters:
        root_path (str): The root directory of the project.

    Returns:
        None
    """
    logging.info("Starting data cleanup...")

    data_path = os.path.join(root_path, "data")

    if os.path.exists(data_path):
        try:
            shutil.rmtree(data_path)  # Remove the entire data folder
            logging.info(f"Deleted folder: {data_path}")
        except Exception as e:
            logging.error(f"Failed to delete folder {data_path}: {e}")
            return

    # Recreate the data folder structure
    try:
        os.makedirs(data_path)
        logging.info(f"Recreated folder: {data_path}")
    except Exception as e:
        logging.error(f"Failed to recreate folder {data_path}: {e}")

    logging.info("Data cleanup completed successfully.")

if __name__ == "__main__":
    project_root = "."  # Define root path as current directory
    clear_data(project_root)