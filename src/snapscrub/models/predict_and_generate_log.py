import os
import logging
import pandas as pd
from .evaluate_image_models import evaluate_image_models
from src.snapscrub.models.get_model_map import get_model_map

def predict_and_generate_log(root_folder, framework="tensorflow", model_name=None):
    """
    Predict image scores using selected models, save results to log CSV,
    and add rankings for each model.

    Parameters:
        root_folder (str): Root directory of the project.
        framework (str): Framework used for models ('tensorflow' or 'pytorch').
        model_name (str): Specific model to run (e.g., 'clip', 'ResNet101'). If None, runs all models.
    """
    resized_folder = os.path.join(root_folder, "resized")

    image_files = [
        os.path.join(resized_folder, f) for f in os.listdir(resized_folder)
        if f.lower().endswith(("jpg", "jpeg", "png", "bmp"))
    ]
    if not image_files:
        logging.warning(f"No images found in the resized folder for {framework}.")
        return

    model_map = get_model_map(framework)

    if model_name and model_name in model_map:
        model_map = {model_name: model_map[model_name]}
        csv_file_suffix = f"_{model_name}"
    else:
        csv_file_suffix = f"_{framework}"

    logging.info(f"Processing with models: {list(model_map.keys())} using {framework}")

    results = []

    for idx, image_path in enumerate(image_files):
        scores = evaluate_image_models(image_path, model_map, framework)
        if scores:
            results.append(scores)
        if (idx + 1) % 10 == 0 or (idx + 1) == len(image_files):
            logging.info(f"Processed {idx + 1}/{len(image_files)} images using {framework}.")

    df = pd.DataFrame(results)

    for model in model_map.keys():
        if model not in df.columns:
            df[model] = None

    scores_csv_path = os.path.join(root_folder, f"model_scores{csv_file_suffix}.csv")

    for model in model_map.keys():
        if df[model].notnull().any():
            df[f"{model}_rank"] = df[model].rank(ascending=False, method="min")

    df.to_csv(scores_csv_path, index=False)
    logging.info(f"Model scores with rankings saved to {scores_csv_path}")