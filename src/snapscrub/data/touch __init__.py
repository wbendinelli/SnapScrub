from snapscrub.data import create_folders

root_directory = "data"
folders = create_folders(root_directory)
print(f"Folders created: {folders}")