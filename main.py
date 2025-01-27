import os
import logging
from src.snapscrub.data.create_folders import create_folders
from src.snapscrub.data.copy_to_original import copy_to_original
from src.snapscrub.data.convert_images import process_images
from src.snapscrub.data.resize_images import resize_images
from src.snapscrub.data.rename_images import rename_images_in_folder
from src.snapscrub.evaluation.duplicate_removal import remove_duplicate_images
from src.snapscrub.models.predict_and_generate_log import predict_and_generate_log
from src.snapscrub.results.transfer_images import transfer_top_images_by_framework

logging.basicConfig(level=logging.INFO)

def main():
    root_path = "data"
    folders = create_folders(root_path)

    source_path = "/Users/wbendinelli/Downloads/teste_photo"
    copy_to_original(source_path, folders["original"])

    # Convert HEIC images and copy other image formats
    logging.info("Processing images (conversion and copying)...")
    process_images(folders["original"], folders["converted"])

    # Rename images before further processing
    mapping_path = os.path.join(root_path, "name_mapping.csv")
    rename_images_in_folder(folders["converted"], mapping_path)

    # Resize images after conversion and renaming
    resize_images(folders["converted"], folders["resized"])

    # Remove duplicate images using multiple similarity measures
    logging.info("Removing duplicate images...")
    removed_images = remove_duplicate_images(
        folder_path=folders["resized"],
        cleaned_folder=folders["cleaned"],
        threshold=0.60  # Ajuste o limiar conforme necessário
    )
    logging.info(f"Total duplicates removed: {len(removed_images)}")

    # Generate image predictions using TensorFlow and PyTorch models
    logging.info("Generating image scores...")
    predict_and_generate_log(root_path, framework="tensorflow")
    predict_and_generate_log(root_path, framework="pytorch")

    # Transfer top-ranked images to results folder
    logging.info("Transferring top-ranked images to results...")
    num_images_to_transfer = 5  # Defina o número de imagens a serem transferidas
    transfer_top_images_by_framework(
        tf_csv_path=os.path.join(root_path, "model_scores_tensorflow.csv"),
        pt_csv_path=os.path.join(root_path, "model_scores_pytorch.csv"),
        name_mapping_path=mapping_path,
        original_folder=folders["original"],
        results_folder=folders["results"],
        num_images=num_images_to_transfer
    )

    logging.info("Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()