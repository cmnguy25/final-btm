from PIL import Image
import os

# Ensure the 'test' directory exists
os.makedirs('test', exist_ok=True)

# Open the original image
original_image_path = 'dataset2/nests/DJI_20240425080042_0014_V.JPG'  # Replace with your actual image file
original_image = Image.open(original_image_path)

# Extract the base name of the original image without the extension
original_base_name = os.path.splitext(os.path.basename(original_image_path))[0]

# Get the dimensions of the original image
original_width, original_height = original_image.size

# Calculate the dimensions of each small section
small_width = original_width // 7
small_height = original_height // 7
print(small_width, small_height)

# Loop to create and save the smaller sections
for i in range(7):
    for j in range(7):
        # Calculate the coordinates of the current section
        left = i * small_width
        upper = j * small_height
        right = (i + 1) * small_width
        lower = (j + 1) * small_height
        
        # Crop the section from the original image
        small_image = original_image.crop((left, upper, right, lower))
        
        # Save the small image to the 'test' directory
        small_image.save(f'test/{original_base_name}_small_image_{i}_{j}.jpg')

print("Images have been successfully saved in the 'test' directory.")