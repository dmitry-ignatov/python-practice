# Task API

Небольшой REST API для управления задачами на FastAPI.

Данные хранятся в памяти, поэтому проект сосредоточен именно на маршрутах и HTTP-поведении без базы данных.

## Endpoints

- `GET /tasks` — список задач;
- `GET /tasks/{id}` — одна задача;
- `POST /tasks` — создание;
- `PATCH /tasks/{id}` — изменение;
- `DELETE /tasks/{id}` — удаление.

Для отсутствующих задач возвращается `404 Not Found`. Тело POST/PATCH проверяется через Pydantic-модели.

## Тесты

В проекте 9 тестов через `pytest` и `TestClient`: успешные сценарии, 404 и сброс состояния между тестами через fixture с `autouse=True`.

## Запуск

1. `python -m pip install -r requirements.txt`
2. `python -m fastapi dev task_api.py`

Swagger после запуска: `http://127.0.0.1:8000/docs`

Тесты: `python -m pytest -v`