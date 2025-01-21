import os
import shutil

def clear_data_folder(data_root):
    """
    Remove all files inside the data directories but keep the folder structure.

    Parameters:
        data_root (str): Path to the root 'data' directory.
    """
    if not os.path.exists(data_root):
        print(f"Directory {data_root} does not exist.")
        return
    
    subfolders = ["original", "resized", "converted", "cleaned", "results"]

    for subfolder in subfolders:
        folder_path = os.path.join(data_root, subfolder)
        if os.path.exists(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
        else:
            os.makedirs(folder_path)
            print(f"Created missing folder: {folder_path}")

    print("Data folder cleaned successfully!")

if __name__ == "__main__":
    data_root_path = os.path.join(os.getcwd(), "data")  # Adjust this path if necessary
    clear_data_folder(data_root_path)