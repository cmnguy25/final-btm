import os

def delete_non_v_files(directory):
    for filename in os.listdir(directory):
        # Full path of the file
        file_path = os.path.join(directory, filename)
        # Check if it's a file and doesn't end with '_v' before the extension
        if os.path.isfile(file_path) and not filename.lower().endswith('_v.jpg'):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# Path to your images folder
images_folder = "images5/"
delete_non_v_files(images_folder)