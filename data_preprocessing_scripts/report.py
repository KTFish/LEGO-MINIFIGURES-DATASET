import os
from typing import Tuple
import config


def count_images(dataset_path: str) -> Tuple[int, int]:
    """Counts images in given dataset.

    Args:
        dataset_path (str): Path to dataset.

    Returns:
        Tuple[int, int]: train images, test images
    """

    train_path = f"{dataset_path}/train"
    train_count = len(list(train_path.glob("*/*.jpg")))

    test_path = f"{dataset_path}/test"
    test_count = len(list(test_path.glob("*/*.jpg")))

    print(f"Number of images in {dataset_path}:")
    print(f"- Training Set: {train_count}")
    print(f"- Test Set: {test_count}")
    print(f"What gives in total: {test_count + train_count}")

    return train_count, test_count
