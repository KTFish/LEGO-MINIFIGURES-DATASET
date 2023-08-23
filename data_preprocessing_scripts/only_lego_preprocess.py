# Script for preprocessing the only_lego_dataset (Consisting of pure Lego Minifigures images).
import os
import PIL
from PIL import Image
import config
import numpy as np
from tqdm import tqdm


def create_folder_structure() -> None:
    path = "./only_lego_dataset_preprocessed"
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

    if height > width:
        margin_size = (height - width) // 2
        margin = np.full((height, margin_size, 3), 255, dtype=np.uint8)  # Adjust dtype

        extended_image_array = np.concatenate((margin, image_array, margin), axis=1)
        extended_image = Image.fromarray(extended_image_array)
        return extended_image
    return image


def preprocess_dataset() -> None:
    create_folder_structure()
    dataset_path = os.path.join(".", "only_lego_dataset")
    assert os.path.exists(dataset_path), "Lack of dataset to be processed."

    # For progress monitoring
    # images_done = 0
    # num_images = len(os.listdir(dataset_path))

    # Preprocessing Loop
    # for image_name in os.listdir(dataset_path):
    images = os.listdir(dataset_path)
    for image_name in tqdm(images):
        # Get path to the original image
        image_path = os.path.join(dataset_path, image_name)

        # Extend image (add margins so that it becomes a square)
        extended_image = add_margins(image_path)

        # Save the extended image
        save_path = os.path.join(".", "only_lego_dataset_preprocessed", image_name)
        extended_image.save(save_path)

        # Monitor progress
        # images_done += 1
        # if images_done % 100 == 0:
        #     print(f"Preprocessed images: {images_done} / {num_images}")


if __name__ == "__main__":
    preprocess_dataset()
