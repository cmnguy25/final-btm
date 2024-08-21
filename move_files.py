import os
import random
import shutil

# Define the input and output directories
input_directory = 'dataset/no_nests'
archive_directory = 'archive'

# Ensure the archive directory exists
os.makedirs(archive_directory, exist_ok=True)

# Get a list of all image files in the input directory
image_files = [f for f in os.listdir(input_directory) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Shuffle the list of image files randomly
random.shuffle(image_files)

# Calculate the number of images to move
num_images_to_move = len(image_files) // 2

# Move half of the images to the archive directory
for i in range(num_images_to_move):
    src_path = os.path.join(input_directory, image_files[i])
    dest_path = os.path.join(archive_directory, image_files[i])
    shutil.move(src_path, dest_path)

print(f"Moved {num_images_to_move} images to the 'archive' directory.")