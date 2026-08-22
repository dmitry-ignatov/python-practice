import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str



def connect_database():
    connection = sqlite3.connect("tasks.db")
    connection.execute("""
                        CREATE TABLE IF NOT EXISTS tasks 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        title TEXT)
                        """)
    connection.commit()

    return connection


def show_tasks(connection):
    cursor = connection.execute("SELECT id, title FROM tasks ORDER BY id ASC")
    tasks = cursor.fetchall()
    for i, task in enumerate(tasks):
        tasks_dict = {}
        tasks_dict["id"] = task[0]
        tasks_dict["title"] = task[1]
        tasks[i] = tasks_dict

    return tasks


def show_task(connection, task_id):
    cursor = connection.execute("SELECT id, title FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    if task is not None:
        task_dict = {}
        task_dict["id"] = task[0]
        task_dict["title"] = task[1]

        return task_dict

    else:
        return None



@app.get("/tasks")
def get_tasks():
    connection = connect_database()
    tasks = show_tasks(connection)
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    connection = connect_database()
    task = show_task(connection, task_id)
    if task is not None:
        return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    created_task = task.title
    connection = connect_database()
    cursor = connection.execute("INSERT INTO tasks (title) VALUES (?)", (created_task,))
    connection.commit()

    return {"id": cursor.lastrowid, "title": created_task}


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    updated_task = task_update.title
    connection = connect_database()
    if show_task(connection, task_id) is not None:
        connection.execute("UPDATE tasks SET title = ? WHERE id = ?", (updated_task, task_id))
        connection.commit()

        return {"id": task_id, "title": updated_task}

    raise HTTPException(
            status_code=404,
            detail="Task not found"
        )




