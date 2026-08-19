from fastapi.testclient import TestClient
from task_api import app
import pytest

import task_api


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_tasks():
    task_api.tasks = [
        {"id": 1, "title": "Купить хлеб"},
        {"id": 2, "title": "Выучить FastAPI"}
    ]



def test_root():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {"message": "Task API"}


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200

    assert response.json() == [
        {"id": 1, "title": "Купить хлеб"},
        {"id": 2, "title": "Выучить FastAPI"}
    ]


def test_get_task():
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Купить хлеб"}


def test_get_task_not_found():
    response = client.get("/tasks/3")

    assert response.status_code == 404
    assert response.json() == {'detail': 'Task not found'}


def test_create_task():
    response = client.post("/tasks", json={"title": "Новая задача"})

    assert response.status_code == 201
    assert response.json() == {"id": 3, "title": "Новая задача"}


def test_patch_task():
    response = client.patch("/tasks/2", json={"title": "Новая задача"})

    assert response.status_code == 200
    assert response.json() == {"id": 2, "title": "Новая задача"}


def test_patch_task_not_found():
    response = client.patch("/tasks/3", json={"title": "Новая задача"})

    assert response.status_code == 404
    assert response.json() == {'detail': 'Task not found'}


def test_delete_task():
    response = client.delete("/tasks/2")

    assert response.status_code == 200
    assert response.json() == {"id": 2, "title": "Выучить FastAPI"}


def test_delete_task_not_found():
    response = client.delete("/tasks/3")

    assert response.status_code == 404
    assert response.json() == {'detail': 'Task not found'}
