from json_config_validator import (is_dict, get_missing_fields, get_incorrect_type_fields, 
                                   get_invalid_value_fields, check_fields_errors, get_json, 
                                   show_json_content, show_fields_errors
                                   )
import pytest

@pytest.mark.parametrize(
        "data, expected",
        [
            ({}, True),
            ([], False)
        ]
)
def test_is_dict(data, expected):
    assert is_dict(data) == expected


@pytest.mark.parametrize(
        "test_dict, expected",
        [
            (
            {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": 100,
        "log_level": "TRACE"
            }, ["log_level"]
            ),

            (
            {
        "app_name": "  ",
        "debug": True,
        "max_users": 100,
        "log_level": "INFO"
            }, ["app_name"]
            ),

            (
            {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": 0,
        "log_level": "INFO"
            }, ["max_users"]
            ),

            (
            {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": 100,
        "log_level": "INFO"
            }, []   
            )
        ]
)
def test_get_invalid_value_fields_returns_expected_result(test_dict, expected):
    
    assert get_invalid_value_fields(test_dict, [], []) == expected


def test_get_missing_fields_returns_missing_field():
    test_dict = {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": 100
    }

    assert get_missing_fields(test_dict) == ["log_level"]


def test_get_missing_fields_returns_empty_list_for_complete_config():
    test_dict = {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": 100,
        "log_level": "INFO"
    }
    
    assert get_missing_fields(test_dict) == []


def test_get_incorrect_type_fields_rejects_bool_for_max_users():
    test_dict = {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": True,
        "log_level": "INFO"
    }

    assert get_incorrect_type_fields(test_dict) == ["max_users"]


def test_get_incorrect_type_fields_returns_empty_list_for_correct_types():
    test_dict = {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": 100,
        "log_level": "INFO"
    }

    assert get_incorrect_type_fields(test_dict) == []


def test_get_invalid_value_fields_skips_field_with_incorrect_type():
    test_dict = {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": "100",
        "log_level": "INFO"
    }

    assert get_invalid_value_fields(test_dict, [], ["max_users"]) == []


def test_check_fields_errors_returns_all_error_categories():
    test_dict = {
        "app_name": "  ",
        "debug": "yes",
        "max_users": 100,
    }

    assert check_fields_errors(test_dict) == (["log_level"], ["debug"], ["app_name"])


def test_check_fields_errors_returns_empty_lists_for_valid_config():
    test_dict = {
        "app_name": "Task Manager",
        "debug": True,
        "max_users": 100,
        "log_level": "INFO"
    }

    assert check_fields_errors(test_dict) == ([], [], [])


def test_get_json_returns_data_from_valid_file(tmp_path):
    json_path = tmp_path / "config.json"
    json_path.write_text('{"app_name": "Task Manager"}', encoding="utf-8")

    assert get_json(json_path) == {"app_name": "Task Manager"}


def test_get_json_returns_none_for_missing_file(tmp_path):
    json_path = tmp_path / "missing.json"
    assert get_json(json_path) is None


def test_get_json_returns_none_for_invalid_json(tmp_path):
    json_path = tmp_path / "invalid.json"
    json_path.write_text('{"app_name": "}', encoding="utf-8")

    assert get_json(json_path) is None


def test_show_json_content_prints_all_fields(capsys):
    test_dict = {
        "app_name": "Task Manager",
        "debug": True
    }
    show_json_content(test_dict)
    captured = capsys.readouterr()

    assert captured.out == "app_name: Task Manager\ndebug: True\n"


def test_show_fields_errors_prints_all_error_categories(capsys):
    show_fields_errors(
        ["log_level"],
        ["debug"],
        ["app_name"]
    )

    captured = capsys.readouterr()

    assert captured.out == """В JSON файле отсутствуют поля:
'log_level'

В JSON файле неправильный тип данных у:
'debug'

В JSON файле некорректные значения в:
'app_name'

"""


def test_show_fields_errors_prints_nothing_without_errors(capsys):
    show_fields_errors([], [], [])

    captured = capsys.readouterr()

    assert captured.out == ""


def test_get_json_prints_message_for_missing_file(tmp_path, capsys):
    json_path = tmp_path / "missing.json"
    get_json(json_path)
    captured = capsys.readouterr()
    assert captured.out == "Файл JSON не найден\n"


def test_get_json_prints_message_for_invalid_json(tmp_path, capsys):
    json_path = tmp_path / "invalid.json"
    json_path.write_text('{"app_name": "}', encoding="utf-8")
    get_json(json_path)
    captured = capsys.readouterr()
    assert captured.out == "Некорректный формат JSON\n"
