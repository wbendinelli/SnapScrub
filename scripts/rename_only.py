import os
import logging
from src.snapscrub.data.rename_images import rename_images_in_folder

logging.basicConfig(level=logging.INFO)

def run_rename():
    # Defina os caminhos das imagens e do arquivo de mapeamento
    folder_path = "data/resized"
    mapping_path = os.path.join("data", "image_mapping.csv")

    # Verifique se a pasta existe antes de rodar
    if os.path.exists(folder_path):
        rename_images_in_folder(folder_path, mapping_path)
        logging.info("Image renaming completed successfully.")
    else:
        logging.error(f"Folder not found: {folder_path}")

if __name__ == "__main__":
    run_rename()