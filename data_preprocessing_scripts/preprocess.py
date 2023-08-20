import os
import PIL
from PIL import Image
import torch
import config
import torchvision
from torchvision import transforms
import numpy as np


def crop_image(
    image_path: str,
    width_start: int,
    width_end: int,
    height_start: int,
    height_end: int,
) -> PIL.Image:
    """
    Takes path to image and edge point in order to crop an image.
    """

    # Open image and access the dimensions
    image = Image.open(image_path)
    cropped_image = image.crop((width_start, height_start, width_end, height_end))
    return cropped_image


def create_folder_structure(destination_path: str = config.DESTINATION_PATH) -> None:
    """Create folder structure for the transformed dataset like that:
    DESTINATION_PATH
       |
       |----- Category 1
       |----- Category 2
       | ...
       |----- Category n
    """
    if not os.path.exists(destination_path):
        os.makedirs(destination_path, exist_ok=True)
    for category_name in config.CATEGORY_NAMES:
        path = f"{destination_path}/{category_name}"
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)


def add_margins(image_path: str) -> PIL.Image:
    """Adds left and right margins to the image in order to make it a square shaped image (height x height).
    Extending the image does not cut off parts of the figure an allows the image to be a square what will be
    beneficial while using CNN network.

    Args:
        image_path (str): Path to the image.

    Returns:
        PIL.Image: PIL Image object with added white margins.
    """
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)
    height, width, _ = image_array.shape
    # width, height, _ = image_array.shape
    if height > width:
        margin_size = (height - width) // 2
        margin = np.full((height, margin_size, 3), 255, dtype=np.uint8)  # Adjust dtype

        extended_image_array = np.concatenate((margin, image_array, margin), axis=1)
        extended_image = Image.fromarray(extended_image_array)
        return extended_image
    return image


def preprocess_dataset(verbose: bool = False, display_step: int = 100) -> None:
    processed_images = 0

    # Sort images into cateogires (categories are stored in config.py)
    for dir in os.listdir(config.RAW_DATASET_PATH):
        # Assign new category based on the config file
        category = (
            "YELLOW"
            if dir in config.YELLOW
            else "SKIN"
            if dir in config.SKIN
            else "OTHER"
        )
        # Loop through images and do the transformations
        dir_path = f"{config.RAW_DATASET_PATH}/{dir}"
        for image_name in os.listdir(dir_path):
            image_path = f"{dir_path}/{image_name}"
            extended_image = add_margins(image_path)

            save_path = f"{config.DESTINATION_PATH}/{category}/{image_name}"
            extended_image.save(save_path)
            processed_images += 1

            if verbose and processed_images % display_step == 0:
                print(f"Processed {processed_images} / {config.NUM_IMAGES_RAW}")


if __name__ == "__main__":
    create_folder_structure()
    preprocess_dataset(verbose=True)
