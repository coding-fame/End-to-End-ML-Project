import os
import yaml
from mlProject import logger
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
import json
from typing import Any
import joblib


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and return

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml is empty
        e: empty

    Return:
        config_box: config_box type
    """
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)


def create_directory(path_to_directories: list, verbose=True):
    """Take list of directory and create it

    Arguments:
       path_to_directories: list of path directories
       ignore_log (bool, optional): ignore if multiple directories to create. Default to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")


def save_json(path: Path, data: dict):
    """Save json data

    Args:
        path (Path): path to join file
        data (dict): data to be saved in json file

    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Jason file saved at {path}")


def load_json(path: Path) -> ConfigBox:
    """Load json file from path and return

    Args:
        path (Path): path which file reading from

    Return:
        ConfigBox: data as class attribute instead of dict
    """
    with open(path) as f:
        content = json.loads(f)
    logger.info(f"Json File loaded successfully from {path}")
    return ConfigBox(content)


def save_bin(data: Any, path: Path):
    """save file to binary

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
