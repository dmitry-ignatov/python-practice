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



def test_create_task():
    response = client.post("/tasks", json={"title": "Новая задача"})


    assert response.status_code == 201
    assert response.json() == {"id": 3, "title": "Новая задача"}


def test_get_task_404():
    response = client.get("/tasks/10")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_delete_task():
    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Купить хлеб"}
