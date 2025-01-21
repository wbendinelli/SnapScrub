import os
import logging
from src.snapscrub.data.create_folders import create_folders
from src.snapscrub.data.copy_to_original import copy_to_original
from src.snapscrub.data.convert_images import process_all_images
from src.snapscrub.data.resize_images import resize_images
from src.snapscrub.data.rename_images import rename_images_in_folder

logging.basicConfig(level=logging.INFO)

def main():
    # Step 1: Create project folders
    root_path = "data"
    folders = create_folders(root_path)
    
    # Step 2: Copy images to 'original' folder
    source_path = "/Users/wbendinelli/Downloads/teste_photo"
    copy_to_original(source_path, folders["original"])

    # Step 3: Process all images (convert HEIC and copy others)
    process_all_images(folders["original"], folders["converted"])

    # Step 4: Resize images to standard dimensions
    resize_images(folders["converted"], folders["resized"])

    # Step 5: Rename images and generate mapping CSV
    mapping_path = os.path.join(root_path, "name_mapping.csv")
    rename_images_in_folder(folders["resized"], mapping_path)

    logging.info("Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()