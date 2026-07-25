from json_config_validator import is_dict, get_missing_fields, get_incorrect_type_fields


def test_is_dict_returns_true_for_dict():
    assert is_dict({})


def test_is_dict_returns_false_for_list():
    assert not is_dict([])


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