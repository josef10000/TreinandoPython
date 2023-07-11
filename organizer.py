import os
import shutil

 
downloads_folder_path = os.path.join(os.path.expanduser("~"), "Downloads")
desktop_folder_path = os.path.join(os.path.expanduser("~"), "Desktop")

 
for file in os.listdir(downloads_folder_path):
    if file != "folder_organizer.py":   
        filename, file_extension = os.path.splitext(file)
        file_extension = file_extension[1:]

        folder_to_organize_file = os.path.join(downloads_folder_path, file_extension)

        if not os.path.isdir(folder_to_organize_file):
            os.mkdir(folder_to_organize_file)

        shutil.move(os.path.join(downloads_folder_path, file), os.path.join(folder_to_organize_file, file))

for file in os.listdir(desktop_folder_path):
    if file != "folder_organizer.py":   
        filename, file_extension = os.path.splitext(file)
        file_extension = file_extension[1:]

        folder_to_organize_file = os.path.join(desktop_folder_path, file_extension)

        if not os.path.isdir(folder_to_organize_file):
            os.mkdir(folder_to_organize_file)

        shutil.move(os.path.join(desktop_folder_path, file), os.path.join(folder_to_organize_file, file))
