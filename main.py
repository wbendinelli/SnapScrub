from src.snapscrub.data.create_folders import create_folders

def main():
    root_path = "data"
    folders = create_folders(root_path)
    print(f"Pastas criadas: {folders}")
    # Chamar outras funções do pipeline aqui

if __name__ == "__main__":
    main()