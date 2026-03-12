import json
import os

lang = os.getenv("LANG", "en")[:2]

file = f"messages_{lang}.json"

try:
    with open(file) as f:
        messages = json.load(f)
except FileNotFoundError:
    with open("messages_en.json") as f:
        messages = json.load(f)