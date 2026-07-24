from pathlib import Path
import json


def get_json():
    json_path = Path(__file__).parent / "config.json"
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Файл JSON не найден")
    except json.JSONDecodeError:
        print("Некорректный формат JSON")

print(get_json())