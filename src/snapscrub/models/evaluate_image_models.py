import os
import logging
import numpy as np
import torch
from tensorflow.keras.preprocessing import image
from PIL import Image

def evaluate_image_models(image_path, model_map, framework="tensorflow"):
    """
    Evaluate an image using various deep learning models.

    Parameters:
        image_path (str): Path to the image file.
        model_map (dict): Dictionary of models and preprocessors.
        framework (str): Either 'tensorflow' or 'pytorch'.

    Returns:
        dict: Dictionary containing image scores.
    """
    try:
        scores = {"file_name": os.path.basename(image_path)}

        if framework == "tensorflow":
            img = image.load_img(image_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)

            for model_name, (model, preprocess) in model_map.items():
                img_preprocessed = preprocess(img_array)
                features = model.predict(img_preprocessed)
                scores[model_name] = np.linalg.norm(features)

        elif framework == "pytorch":
            img = Image.open(image_path).convert("RGB")
            for model_name, (model, preprocess) in model_map.items():
                img_preprocessed = preprocess(img).unsqueeze(0)
                model.eval()
                with torch.no_grad():
                    features = model(img_preprocessed).flatten()
                scores[model_name] = features.norm().item()

        return scores
    except Exception as e:
        logging.error(f"Error processing image {image_path}: {e}")
        return None