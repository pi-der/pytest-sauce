import yaml
from pathlib import Path


def load_test_data(filename="data.yaml"):
    """Load test data from a YAML file"""
    path = Path(__file__).parent.parent.parent / filename
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_login_data(filename="data.yaml"):
    """Load login test data from a YAML file (deprecated, use load_test_data instead)"""
    return load_test_data(filename)
