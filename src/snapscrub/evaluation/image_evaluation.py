import os
import shutil
import logging
import pandas as pd
from itertools import combinations
from src.snapscrub.evaluation.similarity import calculate_similarity
from src.snapscrub.evaluation.sharpness import calculate_sharpness
from src.snapscrub.evaluation.exposure import calculate_exposure

def evaluate_images_from_folders(resized_folder, cleaned_folder, output_csv, criteria):
    """
    Evaluate images based on similarity, sharpness, and exposure, and move rejected images.

    Parameters:
        resized_folder (str): Path to the folder containing resized images.
        cleaned_folder (str): Path to the folder to move rejected images.
        output_csv (str): Path to save the evaluation report CSV.
        criteria (dict): Dictionary with evaluation thresholds.

    Returns:
        pd.DataFrame: DataFrame containing log of moved images.
    """
    logging.info("Starting evaluation of images from folders...")
    deletion_log = []

    # List images in folder
    image_files = [
        f for f in os.listdir(resized_folder)
        if f.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff'))
    ]
    image_paths = {img: os.path.join(resized_folder, img) for img in image_files}

    # Step 1: Detect duplicates using SSIM
    logging.info("Step 1: Detecting duplicates with SSIM...")
    checked_pairs = set()
    duplicates_groups = {}

    for img1, img2 in combinations(image_files, 2):
        pair = tuple(sorted([img1, img2]))
        if pair in checked_pairs:
            continue

        sim_score = calculate_similarity(image_paths[img1], image_paths[img2])
        if sim_score > criteria["similarity_threshold"]:
            if pair[0] not in duplicates_groups:
                duplicates_groups[pair[0]] = [pair[1]]
            else:
                duplicates_groups[pair[0]].append(pair[1])

        checked_pairs.add(pair)

    # Evaluate duplicates and move lower-quality images
    for main_image, duplicates in duplicates_groups.items():
        best_image = main_image
        best_score = calculate_sharpness(image_paths[main_image]) - abs(calculate_exposure(image_paths[main_image]) - 0.5)

        for image_name in duplicates:
            sharpness_score = calculate_sharpness(image_paths[image_name])
            exposure_score = calculate_exposure(image_paths[image_name])
            total_score = sharpness_score - abs(exposure_score - 0.5)

            if total_score > best_score:
                best_score = total_score
                best_image = image_name

        # Move all duplicates except the best image
        for image_name in duplicates:
            if image_name != best_image:
                shutil.move(image_paths[image_name], os.path.join(cleaned_folder, image_name))
                logging.info(f"Moved duplicate: {image_name}")
                deletion_log.append({"Image Name": image_name, "Reason": "Duplicate SSIM"})

    # Step 2: Evaluate sharpness and exposure for non-duplicates
    logging.info("Step 2: Evaluating sharpness and exposure...")
    remaining_files = [f for f in image_files if f not in duplicates_groups]

    for image_name in remaining_files:
        sharpness_score = calculate_sharpness(image_paths[image_name])
        if sharpness_score < criteria["sharpness_threshold"]:
            shutil.move(image_paths[image_name], os.path.join(cleaned_folder, image_name))
            logging.info(f"Moved: {image_name} due to low sharpness")
            deletion_log.append({"Image Name": image_name, "Reason": "Low sharpness"})

    # Exposure evaluation
    for image_name in remaining_files:
        exposure_score = calculate_exposure(image_paths[image_name])
        if abs(exposure_score - 0.5) > criteria["exposure_tolerance"]:
            shutil.move(image_paths[image_name], os.path.join(cleaned_folder, image_name))
            logging.info(f"Moved: {image_name} due to poor exposure")
            deletion_log.append({"Image Name": image_name, "Reason": "Poor exposure"})

    # Save deletion log
    if deletion_log:
        pd.DataFrame(deletion_log).to_csv(output_csv, index=False)
    logging.info(f"Deletion log saved to {output_csv}")
    return pd.DataFrame(deletion_log)