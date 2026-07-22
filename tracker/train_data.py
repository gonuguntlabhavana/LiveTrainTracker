import json
import os

BASE_DIR = os.path.dirname(__file__)

file_path = os.path.join(BASE_DIR, "trains.json")

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)