import os
import PIL
from PIL import Image
import torch
import config
import torchvision
from torchvision import transforms

def crop_image(image_path: str, width_start: int, width_end: int, height_start: int, height_end: int) -> PIL.Image:
    """
    Takes path to image and edge point in order to crop an image.
    """

    # Open image and access the dimensions
    image = Image.open(image_path)
    cropped_image = image.crop((width_start, height_start, width_end, height_end))
    return cropped_image

def create_folder_ctructure() -> None:
    """Create folder structure for the transformed dataset.
    """
    if not os.path.exists(config.DESTINATION_PATH):
        os.makedirs(config.DESTINATION_PATH, exist_ok=True)
    for category_name in config.CATEGORY_NAMES:
        path = f"{config.DESTINATION_PATH}/{category_name}"
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)


transform = transforms.Compose([
    # TODO: Cropping step. Use a separate class? What is the best way of doing this?
    transforms.functional.crop()
    transforms.Resize((config.FINAL_WIDTH, config.FINAL_HEIGHT)),
    transforms.ToPILImage()
    # ? It there even a need transform to a tensor?
])


# Sort images into cateogires (categories are stored in config.py)
for dir in os.listdir(config.RAW_DATASET_PATH):
    # Assign new category based on the config file
    category = 'YELLOW' if dir in config.YELLOW else 'SKIN' if dir in config.SKIN else 'OTHER'
    save_path = f"{config.DESTINATION_PATH}/{category}"

    # Loop through images and do the transformations
    print(f"Images form {dir} assigned to category {category}. Transforming images...")
    for image_name in os.listdir(dir):
        image_path = f"{dir}/image_name"
        image = Image.open(image_path)

        # Transform and save the image
        transformed_image = transform(image)
        transformed_image.save(save_path)
    