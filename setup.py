from src.snapscrub.data.create_folders import create_folders

root_path = "data"
folders = create_folders(root_path)
print(f"Pastas criadas: {folders}")