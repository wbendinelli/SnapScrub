import os
import logging
from src.snapscrub.data.create_folders import create_folders
from src.snapscrub.data.copy_to_original import copy_to_original
from src.snapscrub.data.convert_images import convert_and_copy_images
from src.snapscrub.data.resize_images import resize_images
from src.snapscrub.data.rename_images import rename_images_in_folder
from src.snapscrub.evaluation import calculate_similarity, calculate_sharpness, calculate_exposure, calculate_hash

logging.basicConfig(level=logging.INFO)

def main():
    root_path = "data"
    folders = create_folders(root_path)
    
    source_path = "/Users/wbendinelli/Downloads/teste_photo"
    copy_to_original(source_path, folders["original"])

    # Convert HEIC images and copy other image formats
    convert_and_copy_images(folders["original"], folders["converted"])

    # Resize images after conversion and transfer
    resize_images(folders["converted"], folders["resized"])

    # Rename images sequentially and save mapping
    mapping_path = os.path.join(root_path, "image_mapping.csv")
    rename_images_in_folder(folders["resized"], mapping_path)

    # Evaluate image quality
    test_image = os.path.join(folders["resized"], "1.jpg")
    if os.path.exists(test_image):
        logging.info(f"Sharpness: {calculate_sharpness(test_image)}")
        logging.info(f"Exposure: {calculate_exposure(test_image)}")

        # Check for duplicate detection
        hash_value = calculate_hash(test_image)
        logging.info(f"Image hash: {hash_value}")
    else:
        logging.error(f"Test image not found: {test_image}")

    logging.info("Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()