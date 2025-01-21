import os
import logging
import pandas as pd

def rename_images_in_folder(folder_path, mapping_path):
    """
    Rename images in the specified folder sequentially and save the mapping to a CSV file.

    Parameters:
        folder_path (str): Path to the folder containing the images.
        mapping_path (str): Path to save the name mapping CSV.

    Returns:
        pd.DataFrame: DataFrame containing the mapping of original to renamed files.
    """
    if not os.path.exists(folder_path):
        logging.error(f"Folder not found: {folder_path}")
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff'))]
    if not files:
        logging.warning("No image files found in the folder.")
        return pd.DataFrame(columns=["original_name", "file_name"])

    files.sort()
    mapping = []

    for idx, file_name in enumerate(files):
        old_path = os.path.join(folder_path, file_name)
        new_name = f"{idx + 1}{os.path.splitext(file_name)[1]}"
        new_path = os.path.join(folder_path, new_name)
        try:
            os.rename(old_path, new_path)
            mapping.append({"original_name": file_name, "file_name": new_name})
        except Exception as e:
            logging.error(f"Error renaming {file_name}: {e}")

    mapping_df = pd.DataFrame(mapping)
    try:
        mapping_df.to_csv(mapping_path, index=False)
        logging.info(f"Name mapping saved to {mapping_path}")
    except Exception as e:
        logging.error(f"Error saving name mapping CSV: {e}")
        raise e

    return mapping_df