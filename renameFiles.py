import os

folder_path = "./"
new_folder_path = "converted"

print(os.listdir(folder_path))

# Just change the name of this variable
new_name = "265x250"


def rename_files(folder_path, new_name):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if file_name == "renameFiles.py":
            continue
        # Construct the new file name with the specified string
        new_file_name = new_name + "_" + file_name

        # Build the full paths of the original and new files
        original_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(original_path, new_path)
        print(f"Renamed {file_name} to {new_file_name}"

rename_files(folder_path, new_name)
