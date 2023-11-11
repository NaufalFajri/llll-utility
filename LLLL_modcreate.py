import os
import shutil
import binascii
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide the main window

def add_hex_and_move_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    hex_ab_00 = binascii.unhexlify('AB00')
    if content.startswith(hex_ab_00):
        print(f"Hex 'AB 00' already present in file: {file_path}")
    else:
        new_content = hex_ab_00 + content
        file_name = os.path.basename(file_path)
        folder_name = '_'.join(file_name.split()[:2])  # Limit folder name to two words
        folder_name = folder_name[:2]  # Merge folder name to two characters
        new_folder_path = os.path.join(os.path.dirname(file_path), folder_name)

        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        new_file_path = os.path.join(new_folder_path, file_name)
        if content.startswith(b'UnityFS'):
            new_file_path = os.path.splitext(new_file_path)[0]
        with open(new_file_path, 'wb') as new_file:
            new_file.write(new_content)
        os.remove(file_path)
        print(f"Hex 'AB 00' added, file moved to folder: {new_folder_path}")

def process_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            add_hex_and_move_file(file_path)

# Prompt for directory path

directory_path = filedialog.askdirectory(title="Locate Assets Folder")
if directory_path:
    print(f"Selected folder: {directory_path}")
else:
    print("No folder selected")
    sys.exit(1)
process_directory(directory_path)
