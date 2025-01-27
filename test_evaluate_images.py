import os
import logging
from src.snapscrub.evaluation.image_evaluation import evaluate_images_from_folders

# Configurar logging para saída informativa
logging.basicConfig(level=logging.INFO)

def test_evaluate_images():
    # Definir os caminhos das pastas
    resized_folder = "data/resized"
    cleaned_folder = "data/cleaned"
    output_csv = "data/results/evaluation_report.csv"

    # Definir critérios de avaliação
    criteria = {
        "similarity_threshold": 0.80,
        "sharpness_threshold": 80,
        "exposure_tolerance": 0.2
    }

    logging.info("Starting test for image evaluation...")
    evaluate_images_from_folders(resized_folder, cleaned_folder, output_csv, criteria)

    logging.info(f"Evaluation completed. Check the report at {output_csv}")

if __name__ == "__main__":
    test_evaluate_images()