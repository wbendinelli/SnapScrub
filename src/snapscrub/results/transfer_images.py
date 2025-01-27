import os
import shutil
import logging
import pandas as pd

def transfer_top_images_by_framework(tf_csv_path, pt_csv_path, name_mapping_path, original_folder, results_folder, num_images=20):
    """
    Transfer top-ranked original images to subfolders in the results folder for each framework (TensorFlow/PyTorch).

    Parameters:
        tf_csv_path (str): Path to the TensorFlow scores CSV.
        pt_csv_path (str): Path to the PyTorch scores CSV.
        name_mapping_path (str): Path to the name mapping CSV (resized-to-original mapping).
        original_folder (str): Path to the folder containing original images.
        results_folder (str): Path to save the selected images.
        num_images (int): Number of top-ranked images to transfer for each model.
    """
    os.makedirs(results_folder, exist_ok=True)
    tensorflow_results = os.path.join(results_folder, "tensorflow_models")
    pytorch_results = os.path.join(results_folder, "pytorch_models")
    os.makedirs(tensorflow_results, exist_ok=True)
    os.makedirs(pytorch_results, exist_ok=True)

    mapping_df = pd.read_csv(name_mapping_path)
    mapping_df["original_name_normalized"] = mapping_df["original_name"].str.strip().str.lower()
    mapping_df["file_name"] = mapping_df["file_name"].str.strip().str.lower()

    available_files = {
        f.lower(): os.path.abspath(os.path.join(original_folder, f))
        for f in os.listdir(original_folder)
    }

    for framework, csv_path, target_folder in [
        ("TensorFlow", tf_csv_path, tensorflow_results),
        ("PyTorch", pt_csv_path, pytorch_results)
    ]:
        if not os.path.exists(csv_path):
            logging.warning(f"CSV file for {framework} not found: {csv_path}")
            continue

        scores_df = pd.read_csv(csv_path)
        scores_df["file_name"] = scores_df["file_name"].str.strip().str.lower()

        merged_df = pd.merge(scores_df, mapping_df, how="left", on="file_name")

        ranking_columns = [col for col in scores_df.columns if col.endswith("_rank")]
        logging.info(f"Ranking columns identified for {framework}: {ranking_columns}")

        for ranking_column in ranking_columns:
            model_name = ranking_column.replace("_rank", "")
            model_folder = os.path.join(target_folder, model_name)
            os.makedirs(model_folder, exist_ok=True)

            top_images = merged_df.sort_values(by=ranking_column, ascending=True).head(num_images)
            transferred_files = []

            for _, row in top_images.iterrows():
                original_name_normalized = row["original_name_normalized"]
                original_path = available_files.get(original_name_normalized)

                if original_path:
                    try:
                        destination_path = os.path.join(model_folder, os.path.basename(original_path))
                        shutil.copy(original_path, destination_path)
                        transferred_files.append(original_name_normalized)
                        logging.info(f"Transferred: {os.path.basename(original_path)} to {model_folder}")
                    except Exception as e:
                        logging.error(f"Error transferring {os.path.basename(original_path)}: {e}")
                else:
                    logging.warning(f"File not found: {original_name_normalized}")

            transfer_log_path = os.path.join(model_folder, "transfer_log.csv")
            top_images["transferred"] = top_images["original_name_normalized"].isin(transferred_files)
            top_images.to_csv(transfer_log_path, index=False)
            logging.info(f"Transfer log saved for model {model_name} at {transfer_log_path}")