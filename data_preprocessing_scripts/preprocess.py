import os
import PIL
from PIL import Image
import config
import numpy as np
from random import random


def create_folder_structure(destination_path: str = config.DESTINATION_PATH) -> None:
    """Create folder structure for the transformed dataset like that:
    DESTINATION_PATH
       |
       |----- Train
       |        |
       |        |----- Category 1
       |        |----- Category 2
       |        | ...
       |        |----- Category 2
       |
       |----- Test
       |        |
       |        |----- Category 1
       |        |----- Category 2
       |        | ...
       |        |----- Category 2
    """
    for path in [config.TRAIN_DATASET_PATH, config.TEST_DATASET_PATH]:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        for category_name in config.CATEGORY_NAMES:
            full_path = f"{path}/{category_name}"
            if not os.path.exists(full_path):
                os.makedirs(full_path, exist_ok=True)


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

    if height > width:
        margin_size = (height - width) // 2
        margin = np.full((height, margin_size, 3), 255, dtype=np.uint8)  # Adjust dtype

        extended_image_array = np.concatenate((margin, image_array, margin), axis=1)
        extended_image = Image.fromarray(extended_image_array)
        return extended_image
    return image


# def preprocess_directory(dir: str) -> int:
#     """Transforms images from the directory of given name (not path).

#     Args:
#         dir (str): Name of directory (category from raw dataset).

#     Returns:
#         int: Number of images in that directory (used for progress monitoring).
#     """
#     # Assign new category based on the config file
#     category = (
#         "YELLOW" if dir in config.YELLOW else "SKIN" if dir in config.SKIN else "OTHER"
#     )
#     # Loop through images and do the transformations
#     dir_path = rf"{config.RAW_DATASET_PATH}/{dir}"
#     for image_name in os.listdir(dir_path):
#         image_path = rf"{dir_path}/{image_name}"
#         extended_image = add_margins(image_path)

#         set_name = "train" if random() > 0.2 else "test"
#         save_path = rf"{config.DESTINATION_PATH}/{set_name}/{category}/{image_name}"

#         # TODO: Issue with brackets??
#         save_path = save_path.replace("(", "").replace(")", "")
#         extended_image.save(save_path)

#     return len(os.listdir(dir_path))


def preprocess_dataset(verbose: bool = True) -> None:
    """Runs the data preprocessing pipeline.

    Args:
        verbose (bool, optional): If set to True the function prints information about the progress. Defaults to True.
    """
    create_folder_structure()
    processed_images = 0

    # Sort images into cateogires (categories are stored in config.py)
    for dir in os.listdir(config.RAW_DATASET_PATH):
        processed_images += preprocess_directory(dir)
        if verbose:
            print(f"Processed {processed_images} / {config.NUM_IMAGES_RAW}")


def test_folder_structure() -> None:
    assert os.path.exists(r"preprocessed_dataset\train\YELLOW")
    assert os.path.exists(r"preprocessed_dataset\train\SKIN")
    assert os.path.exists(r"preprocessed_dataset\train\OTHER")
    assert os.path.exists(r"preprocessed_dataset\test\YELLOW")
    assert os.path.exists(r"preprocessed_dataset\test\SKIN")
    assert os.path.exists(r"preprocessed_dataset\test\OTHER")


if __name__ == "__main__":
    # preprocess_dataset(verbose=True)
    # preprocess_directory("star-wars")
    x = "CTY0699-Construction-Worker-Male-Orange-Safety-Vest-Reflective-Stripes-Reddish-Brown-Shirt-Dark-Tan-Legs-Red-Construction-Helmet-with-Black-Headphones-Orange-Safety-Glasses.png"
    y = "CTY0699-Construction-Worker-Male-Orange-Safety-Vest-Reflective-Stripes-Reddish-Brown-Shirt-Dark-Tan-Legs-Red-Construction-Helmet-with-Black-Headphones-Orange-Safety-Glasses.png"
    print(x == y)
# TODO: Solve FileNotFoundError: [Errno 2] No such file or directory: './preprocessed_dataset/YELLOW/CTY0527-Construction-Worke-....
