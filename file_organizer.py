import os
import shutil

# Folder to organize
source_folder = "Test_Files"

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Spreadsheets": [".xlsx", ".xls", ".csv"],
    "Others": []
}

# Check if source folder exists
if not os.path.exists(source_folder):
    print("Test_Files folder not found.")
else:
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()
            category_found = False

            for category, extensions in categories.items():
                if extension in extensions:
                    folder_name = category
                    category_found = True
                    break

            if not category_found:
                folder_name = "Others"

            destination_folder = os.path.join(source_folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(destination_folder, file_name)
            shutil.move(file_path, destination_path)

            print(f"Moved: {file_name} -> {folder_name}")

    print("\nFile organization completed successfully!")