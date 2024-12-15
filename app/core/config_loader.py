# app/core/config_loader.py
import json
import os

class ConfigLoader:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file '{self.config_file}' not found.")
        with open(self.config_file, "r") as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)
