import json
from os import write


def get_grouped_keys(data, path="", keys_set=None):
    if keys_set is None:
        keys_set = set()

    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key
            keys_set.add(current_path)
            get_grouped_keys(value, current_path, keys_set)
    elif isinstance(data, list):
        for item in data:
            get_grouped_keys(item, f"{path}[]", keys_set)

    return keys_set

all_keys = set()
paths = ['san_take_home_json_3.json','san_take_home_json_2.json','san_take_home_json_4.json','san_take_home_json_5.json']
for file_path in paths:
    try:

        with open(file_path, 'r') as f:
            json_data = json.load(f)

        all_keys.update(get_grouped_keys(json_data))

        f.close()

    except FileNotFoundError:
        print("File not found. Please check the path.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")

with open("keys", 'a') as f:
    for k in sorted(all_keys):
        f.write(f"- {k}\n")
