import os
import shutil

# Path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
}

# Organize files
for file_name in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    _, extension = os.path.splitext(file_name)
    extension = extension.lower()

    # Find the correct category
    moved = False
    for folder_name, extensions in file_types.items():
        if extension in extensions:
            destination_folder = os.path.join(downloads_folder, folder_name)

            # Create the folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)

            # Move the file
            shutil.move(file_path, os.path.join(destination_folder, file_name))
            print(f"Moved: {file_name} -> {folder_name}")
            moved = True
            break

    # Move unknown files to "Others"
    if not moved:
        other_folder = os.path.join(downloads_folder, "Others")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(other_folder, file_name))
        print(f"Moved: {file_name} -> Others")

print("Downloads folder has been organized successfully!")