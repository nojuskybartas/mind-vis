import os
from PIL import Image

data_path = "wandb/run-20231027_105637-2l8klv10/files/media/images"
num_columns = 4
num_rows = 5

# get the images
image_file_names = [image_file_name for image_file_name in os.listdir(data_path) if ("samples_test" in image_file_name) and ("full" not in image_file_name)]

data = []

for image_file_name in image_file_names:
    image = Image.open(data_path + "/" + image_file_name)
    epoch = image_file_name.split("_")[2]

    # Calculate the size of each small image including the border
    width, height = image.size
    total_border_width = num_columns + 1  # Borders between images and on the edges
    total_border_height = num_rows + 1
    single_width_with_border = width // num_columns
    single_height_with_border = height // num_rows

    for row in range(num_rows):
        row_images = []
        for col in range(num_columns):
            # Calculate the coordinates of the current small image
            left = col * single_width_with_border + 1  # Skip the left border
            top = row * single_height_with_border + 1  # Skip the top border
            right = left + single_width_with_border - 2  # Skip the right border
            bottom = top + single_height_with_border - 2  # Skip the bottom border

            # Ensure that the right and bottom values do not exceed the image dimensions
            right = min(right, width)
            bottom = min(bottom, height)

            # Crop and store the current small image
            small_image = image.crop((left, top, right, bottom))
            
            row_images.append(small_image)

        data.append({
            "epoch": epoch,
            "GT": row_images[0],
            "samples": row_images[1:],
        })

