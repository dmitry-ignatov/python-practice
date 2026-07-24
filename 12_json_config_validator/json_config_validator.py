from pathlib import Path
import json


def is_dict(data):
    return isinstance(data, dict)
    

def get_json(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Файл JSON не найден")
    except json.JSONDecodeError:
        print("Некорректный формат JSON")


def get_missing_fields(data):
    required_fields = ["app_name", "debug", "max_users", "log_level"]
    missing_fields = []
    for key in required_fields:
        if key not in data:
            missing_fields.append(key)
    return missing_fields


json_path = Path(__file__).parent / "config.json"
data = get_json(json_path)
if data is not None:
    if is_dict(data):
        print(data)
        missing_fields = get_missing_fields(data)
        if missing_fields:
            print(missing_fields)
    else:
        print("Содержимое JSON не является словарем")

