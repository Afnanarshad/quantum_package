import yaml
from typing import Dict

def load_config(file_path: str) -> Dict:
    """
    Load configuration from a YAML file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Configuration dictionary.
    """
    try:
        with open(file_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        return config or {}  # Handle empty file
    except FileNotFoundError:
        print(f"Config file '{file_path}' not found. Using default parameters.")
        return {}
    except yaml.YAMLError:
        print(f"Error parsing YAML in '{file_path}'. Using default parameters.")
        return {}