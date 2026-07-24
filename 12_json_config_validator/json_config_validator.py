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


def get_incorrect_type_fields(data):
    incorrect_fields = []
    if "app_name" in data and not isinstance(data["app_name"], str):
        incorrect_fields.append("app_name")

    if "debug" in data and not isinstance(data["debug"], bool):
        incorrect_fields.append("debug")

    if "max_users" in data and type(data["max_users"]) is not int:
        incorrect_fields.append("max_users")

    if "log_level" in data and not isinstance(data["log_level"], str):
        incorrect_fields.append("log_level")

    return incorrect_fields


def get_missing_fields(data):
    required_fields = ["app_name", "debug", "max_users", "log_level"]
    missing_fields = []
    for key in required_fields:
        if key not in data:
            missing_fields.append(key)
    return missing_fields


def show_fields_errors(missing_fields, incorrect_fields):
    
    if missing_fields:
        print(f"В JSON файле отсутствуют поля: {missing_fields}")
    
    if incorrect_fields:
        print(f"В JSON файле неправильный тип данных у: {incorrect_fields}")


json_path = Path(__file__).parent / "config.json"
data = get_json(json_path)
if data is not None:
    if is_dict(data):
        print(data)
        missing_fields = get_missing_fields(data)
        incorrect_fields = get_incorrect_type_fields(data)
        show_fields_errors(missing_fields, incorrect_fields)
    else:
        print("Содержимое JSON не является словарем")

