import os
import shutil

def get_downloads_folder():
    """Get the path to the user's Downloads folder."""
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    return downloads_folder

def move_files_to_destination(download_folder):
    """Move files from the Downloads folder to their respective destination folders."""
    destination_folders = {
        'pdf': os.path.join(download_folder, 'pdf'),
        'docx': os.path.join(download_folder, 'docx'),
        'mp4': os.path.join(download_folder, 'mp4'),
        'jpg': os.path.join(download_folder, 'Pictures'),
        'jpeg': os.path.join(download_folder, 'Pictures'),
        'png': os.path.join(download_folder, 'Pictures'),
        'txt': os.path.join(download_folder, 'text_files'),
        'zip': os.path.join(download_folder, 'zip_files'),
        # Add more file types and their corresponding destination folders as needed
    }

    # Create destination folders if they don't exist
    for folder in destination_folders.values():
        os.makedirs(folder, exist_ok=True)

    # Organize files in the Downloads folder
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()
            if file_extension in destination_folders:
                dest_folder = destination_folders[file_extension]
                shutil.move(file_path, dest_folder)
                print(f"Moved {filename} to {dest_folder}")

def main():
    """Main function to organize files in the Downloads folder."""
    download_folder = get_downloads_folder()
    print(f"Organizing files in {download_folder}...")

    try:
        move_files_to_destination(download_folder)
        print("Files organized successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
