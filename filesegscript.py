import os
import shutil
import tkinter as tk
from tkinter import messagebox

def get_downloads_folder():
    """Get the path to the user's Downloads folder."""
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    return downloads_folder

def move_files_to_destination(download_folder):
    """Move files from the Downloads folder to their respective destination folders."""
    destination_folders = {
        # Document files
        'pdf': os.path.join(download_folder, 'pdf'),
        'docx': os.path.join(download_folder, 'docx'),
        'doc': os.path.join(download_folder, 'docx'),
        'txt': os.path.join(download_folder, 'text_files'),
        
        # Video files
        'mp4': os.path.join(download_folder, 'videos'),
        'mkv': os.path.join(download_folder, 'videos'),
        'avi': os.path.join(download_folder, 'videos'),
        'mov': os.path.join(download_folder, 'videos'),
        'wmv': os.path.join(download_folder, 'videos'),
        'flv': os.path.join(download_folder, 'videos'),
        'mpeg': os.path.join(download_folder, 'videos'),
        '3gp': os.path.join(download_folder, 'videos'),
        
        # Image files
        'jpg': os.path.join(download_folder, 'Pictures'),
        'jpeg': os.path.join(download_folder, 'Pictures'),
        'png': os.path.join(download_folder, 'Pictures'),
        'gif': os.path.join(download_folder, 'Pictures'),
        'bmp': os.path.join(download_folder, 'Pictures'),
        'svg': os.path.join(download_folder, 'Pictures'),
        
        # Audio files
        'mp3': os.path.join(download_folder, 'audio'),
        'wav': os.path.join(download_folder, 'audio'),
        'ogg': os.path.join(download_folder, 'audio'),
        'flac': os.path.join(download_folder, 'audio'),
        'aac': os.path.join(download_folder, 'audio'),
        'wma': os.path.join(download_folder, 'audio'),
        
        # Compressed files
        'zip': os.path.join(download_folder, 'zip_files'),
        'rar': os.path.join(download_folder, 'zip_files'),
        '7z': os.path.join(download_folder, 'zip_files'),
        'tar': os.path.join(download_folder, 'zip_files'),
        'gz': os.path.join(download_folder, 'zip_files'),
        'bz2': os.path.join(download_folder, 'zip_files'),
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

    # Show pop-up message after files have been segregated
    messagebox.showinfo("File Segregation Complete", "Easy -EJ")

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
