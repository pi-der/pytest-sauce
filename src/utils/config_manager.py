import yaml
from pathlib import Path

class ConfigLoader:
    def __init__(self, filename="config.yaml"):
        config_path = Path(__file__).parent.parent / filename
        with open(config_path, 'r', encoding='utf-8') as f:
            self._config = yaml.safe_load(f)

    def get(self, key, default=None):
        return self._config.get(key, default)
