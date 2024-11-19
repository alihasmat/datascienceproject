import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """  Read yaml file and return

    Args:
         path_to_yaml (str): Path like input

    Raises:
        ValueError: If yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
       with open(path_to_yaml) as yaml_file:
           content = yaml.safe_load(yaml_file)
           logger.info(f"yaml file: {path_to_yaml} loaded successfully")
           return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
       raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Create list of directories

    Args:
        path_to_directories (list): List of directories
        verbose (bool, optional): Print message. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """ Save json file

    Args:
        path (Path): Path to json file
        data (dict): Data to save in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"Data saved in json file: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ Load json file

    Args:
        path (Path): Path to json file

    Returns:
        ConfigBox: ConfigBox type
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Data loaded from json file: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ Save binary file

    Args:
        data (Any): Data to save
        path (Path): Path to save
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """ Load binary file

    Args:
        path (Path): Path to file

    Returns:
        Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"Data loaded from file: {path}")
    return data