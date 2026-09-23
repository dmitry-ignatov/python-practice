# JSON Config Validator

Валидатор JSON-конфигурации с отдельной проверкой структуры, типов и значений.

Программа ожидает поля `app_name`, `debug`, `max_users` и `log_level`. Ошибки разделяются на три группы: отсутствующие поля, неправильные типы и недопустимые значения. Некорректный JSON и отсутствие файла обрабатываются отдельно.

## Пример ожидаемой конфигурации

`{"app_name": "Task Manager", "debug": true, "max_users": 100, "log_level": "INFO"}`

## Тесты

В проекте 25 тестовых сценариев. Проверяются положительные и отрицательные случаи, ошибки файла, вывод программы и основные ветки `main()`.

Используются `pytest`, параметризация, собственная fixture, `tmp_path`, `capsys` и `monkeypatch`.

## Запуск

1. `python -m pip install -r requirements.txt`
2. `python json_config_validator.py`

Тесты: `python -m pytest -v`