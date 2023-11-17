import os
from PIL import Image
from eval_metrics import get_similarity_metric
import numpy as np
# import torch
from torchvision import transforms
# from torchmetrics.image.fid import FrechetInceptionDistance
# fid = FrechetInceptionDistance(feature=64)

data_path = "wandb/run-20231027_105637-2l8klv10/files/media/images"
num_columns = 4
num_rows = 5

# get the images
image_file_names = [image_file_name for image_file_name in os.listdir(data_path) if ("samples_test" in image_file_name) and ("full" not in image_file_name)]
image_file_names.sort(key= lambda x: int(x.split("_")[2]))

data = []

metric_name = "psm"

for image_file_name in image_file_names:
    image = Image.open(data_path + "/" + image_file_name)
    epoch = image_file_name.split("_")[2]

    print(f"\n\nEpoch {epoch} -------------------", end="\n")

    # Calculate the size of each small image including the border
    width, height = image.size
    total_border_width = num_columns + 1  # Borders between images and on the edges
    total_border_height = num_rows + 1
    single_width_with_border = width // num_columns
    single_height_with_border = height // num_rows

    print ("\n" + f"\t{metric_name}"*(num_columns-1))
    for row in range(num_rows):
        row_images = []
        gt_tensor = None
        metric_values = []
        print("\n")
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

           # Convert PIL Image to NumPy array
            numpy_image = np.array(small_image)

            # Add an extra dimension to get 'n' dimension
            # Assuming n=1 for a single image in the batch
            batched_image = np.expand_dims(numpy_image, axis=0)
            
            if col == 0:
                print(f"{row}:", end="\t")
                gt_tensor = numpy_image
            else:
                metric_value = round(get_similarity_metric(gt_tensor, numpy_image, method="metrics-only", metric_name=metric_name), 2)
                metric_values.append(metric_value)
                print(metric_value, end="\t")
        
        data.append({
            "epoch": epoch,
            "GT": row_images[0],
            "samples": row_images[1:],
        })  

    average = round(sum(metric_values)/len(metric_values), 2)
    minimum = min(metric_values)
    print(f"\navg: \t{average}", end="\n")
    print(f"min: \t{minimum}", end="\n")
    