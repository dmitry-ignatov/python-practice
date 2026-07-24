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


def get_incorrect_type_fields(data):
    incorrect_type_fields = []
    if "app_name" in data and not isinstance(data["app_name"], str):
        incorrect_type_fields.append("app_name")

    if "debug" in data and not isinstance(data["debug"], bool):
        incorrect_type_fields.append("debug")

    if "max_users" in data and type(data["max_users"]) is not int:
        incorrect_type_fields.append("max_users")

    if "log_level" in data and not isinstance(data["log_level"], str):
        incorrect_type_fields.append("log_level")

    return incorrect_type_fields


def get_invalid_value_fields(data, missing_fields, incorrect_type_fields):
    invalid_value_fields = []

    if not ("app_name" in missing_fields or "app_name" in incorrect_type_fields):
        if not data["app_name"].strip():
            invalid_value_fields.append("app_name")

    if not ("log_level" in missing_fields or "log_level" in incorrect_type_fields):
        allowed_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if data["log_level"] not in allowed_log_levels:
            invalid_value_fields.append("log_level")

    if not ("max_users" in missing_fields or "max_users" in incorrect_type_fields):
        if data["max_users"] <= 0:
            invalid_value_fields.append("max_users")

    return invalid_value_fields


def check_fields_errors(data):
    missing_fields = get_missing_fields(data)
    incorrect_type_fields = get_incorrect_type_fields(data)
    invalid_value_fields = get_invalid_value_fields(data, missing_fields, incorrect_type_fields)
    return missing_fields, incorrect_type_fields, invalid_value_fields


def show_fields_errors(missing_fields, incorrect_type_fields, invalid_value_fields):
    
    if missing_fields:
        print("В JSON файле отсутствуют поля:")
        for field in missing_fields:
            print(f"'{field}'")
        print()

    if incorrect_type_fields:
        print("В JSON файле неправильный тип данных у:")
        for field in incorrect_type_fields:
            print(f"'{field}'")
        print()

    if invalid_value_fields:
        print("В JSON файле некорректные значения в:")
        for field in invalid_value_fields:
            print(f"'{field}'")
        print()


def show_json_content(data):
    for key, value in data.items():
        print(f"{key}: {value}")


def main():
    json_path = Path(__file__).parent / "config.json"
    data = get_json(json_path)
    if data is not None:
        if is_dict(data):
            show_json_content(data)
            missing_fields, incorrect_type_fields, invalid_value_fields = check_fields_errors(data)
            show_fields_errors(missing_fields, incorrect_type_fields, invalid_value_fields)
        else:
            print("Содержимое JSON не является словарем")


if __name__ == "__main__":
    main()
