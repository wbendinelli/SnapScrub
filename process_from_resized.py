import os
import logging
from src.snapscrub.evaluation.duplicate_removal import remove_duplicate_images

logging.basicConfig(level=logging.INFO)

def main():
    root_path = "data"
    resized_folder = os.path.join(root_path, "resized")
    cleaned_folder = os.path.join(root_path, "cleaned")

    if not os.path.exists(resized_folder):
        logging.error(f"Resized folder not found: {resized_folder}")
        return

    logging.info("Starting duplicate removal from resized images...")

    removed_images = remove_duplicate_images(
        folder_path=resized_folder,
        cleaned_folder=cleaned_folder,
        threshold=0.90  # Ajuste conforme necessário
    )

    logging.info(f"Total duplicates removed: {len(removed_images)}")
    logging.info("Processing from resized folder completed.")

if __name__ == "__main__":
    main()