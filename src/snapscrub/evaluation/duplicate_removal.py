import os
import shutil
import logging
import imagehash
from itertools import combinations
from src.snapscrub.utils.calculate_phash import calculate_phash
from src.snapscrub.utils.calculate_histogram_similarity import calculate_histogram_similarity
from src.snapscrub.utils.calculate_structural_similarity import calculate_structural_similarity

def remove_duplicate_images(folder_path, cleaned_folder, threshold=0.90):
    """
    Identify and move duplicate images based on multiple similarity measures (pHash, Histogram, SSIM).

    Parameters:
        folder_path (str): Path to the folder containing images.
        cleaned_folder (str): Folder to move duplicate images.
        threshold (float): Similarity threshold (default: 0.90).

    Returns:
        list: A list of removed images.
    """
    logging.info("Starting duplicate detection...")

    if not os.path.exists(cleaned_folder):
        os.makedirs(cleaned_folder)

    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff'))]
    removed_images = []
    checked_pairs = set()
    hashes = {}

    for img1, img2 in combinations(images, 2):
        pair = tuple(sorted([img1, img2]))
        if pair in checked_pairs:
            continue

        path1 = os.path.join(folder_path, img1)
        path2 = os.path.join(folder_path, img2)

        # Verificar se os arquivos ainda existem antes de processá-los
        if not os.path.exists(path1) or not os.path.exists(path2):
            logging.warning(f"Skipping non-existing file: {path1} or {path2}")
            continue

        # Compute Perceptual Hash (pHash) only once per image
        if img1 not in hashes:
            hashes[img1] = calculate_phash(path1)
        if img2 not in hashes:
            hashes[img2] = calculate_phash(path2)

        hash1 = hashes[img1]
        hash2 = hashes[img2]

        if hash1 and hash2:
            try:
                hash_similarity = 1 - (imagehash.hex_to_hash(hash1) - imagehash.hex_to_hash(hash2)) / len(hash1)
            except Exception as e:
                logging.error(f"Error comparing pHash for {img1} and {img2}: {e}")
                continue

            if hash_similarity >= threshold:
                logging.info(f"Duplicate found: {img1} and {img2} (pHash similarity: {hash_similarity:.2f})")
                try:
                    shutil.move(path2, os.path.join(cleaned_folder, img2))
                    removed_images.append(img2)
                except FileNotFoundError:
                    logging.warning(f"File not found while moving: {path2}")
                continue

        # Compute Histogram Similarity
        hist_similarity = calculate_histogram_similarity(path1, path2)
        if hist_similarity >= threshold:
            logging.info(f"Duplicate found: {img1} and {img2} (Histogram similarity: {hist_similarity:.2f})")
            try:
                shutil.move(path2, os.path.join(cleaned_folder, img2))
                removed_images.append(img2)
            except FileNotFoundError:
                logging.warning(f"File not found while moving: {path2}")
            continue

        # Compute SSIM (Structural Similarity Index)
        ssim_score = calculate_structural_similarity(path1, path2)
        if ssim_score >= threshold:
            logging.info(f"Duplicate found: {img1} and {img2} (SSIM similarity: {ssim_score:.2f})")
            try:
                shutil.move(path2, os.path.join(cleaned_folder, img2))
                removed_images.append(img2)
            except FileNotFoundError:
                logging.warning(f"File not found while moving: {path2}")

        checked_pairs.add(pair)

    logging.info(f"Duplicate detection completed. {len(removed_images)} images removed.")
    return removed_images