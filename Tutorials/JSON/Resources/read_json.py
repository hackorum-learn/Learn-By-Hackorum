"""
This code can be used to read the contents of a local JSON file and parse it into an indexable object through python.
"""

import json
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(FILE_PATH, "aquarium_level.json")

with open(JSON_PATH) as file:
    data = json.load(file)

# Pretty prints the JSON data in alphabetical order
print(json.dumps(data, sort_keys=True, indent=2))

print(data.get("generators"))
