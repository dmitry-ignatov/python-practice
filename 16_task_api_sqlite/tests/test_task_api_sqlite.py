from fastapi.testclient import TestClient
from task_api_sqlite import app
import pytest
import task_api_sqlite


client = TestClient(app)


@pytest.fixture(autouse=True)
def test_database(tmp_path, monkeypatch):
    test_database_path = tmp_path / "tasks.db"

    monkeypatch.setattr(
        task_api_sqlite,
        "DATABASE_PATH",
        test_database_path
    )

    task_api_sqlite.init_database()

    connection = task_api_sqlite.connect_database()
    connection.execute("INSERT INTO tasks (title) VALUES (?)", ("Купить хлеб",))
    connection.execute("INSERT INTO tasks (title) VALUES (?)", ("Выучить FastAPI",))

    connection.commit()
    connection.close()



# GET

def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "Купить хлеб"}, {"id": 2, "title": "Выучить FastAPI"}]


def test_get_task_404():
    response = client.get("/tasks/10")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}



# POST

def test_create_task():
    response = client.post("/tasks", json={"title": "Новая задача"})


    assert response.status_code == 201
    assert response.json() == {"id": 3, "title": "Новая задача"}


def test_create_task_empty_json():
    response = client.post("/tasks", json={})

    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "missing"


def test_create_task_empty_title():
    response = client.post("/tasks", json={"title": ""})

    assert response.status_code == 201
    assert response.json() == {"id": 3, "title": ""}



# UPDATE

def test_update_task():
    response = client.patch("/tasks/1", json={"title": "Купить молоко"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Купить молоко"}


def test_update_task_empty_json():
    response = client.patch("/tasks/1", json={})

    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "missing"


def test_update_task_empty_title():
    response = client.patch("/tasks/1", json={"title": ""})
    
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": ""}


def test_update_task_404():
    response = client.patch("/tasks/10", json={"title": "Купить молоко"})

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}



# DELETE

def test_delete_task():
    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Купить хлеб"}


def test_delete_task_404():
    response = client.delete("/tasks/10")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


