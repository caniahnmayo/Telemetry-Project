import json


def get_unique_non_decimal_values(data, target_key, found_values=None):
    if found_values is None:
        found_values = set()

    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                if isinstance(value, (int, str)) and not isinstance(value, (float, bool)):
                    found_values.add(value)

            get_unique_non_decimal_values(value, target_key, found_values)

    elif isinstance(data, list):
        for item in data:
            get_unique_non_decimal_values(item, target_key, found_values)

    return found_values

all_keys = set()
paths = ['san_take_home_json_3.json','san_take_home_json_2.json','san_take_home_json_4.json','san_take_home_json_5.json']
for file_path in paths:
    try:

        with open(file_path, 'r') as f:
            json_data = json.load(f)

        all_keys.update(get_unique_non_decimal_values(json_data, "FuelLevel"))

        f.close()

    except FileNotFoundError:
        print("File not found. Please check the path.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")

with open("fuel_values", 'a') as f:
    for k in sorted(all_keys):
        f.write(f"- {k}\n")
