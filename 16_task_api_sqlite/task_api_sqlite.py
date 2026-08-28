import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager

DATABASE_PATH = "tasks.db"

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    
    yield


app = FastAPI(lifespan=lifespan)


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str



def connect_database():
    connection = sqlite3.connect(DATABASE_PATH)

    return connection


def init_database():
    connection = connect_database()
    try:
        connection.execute(
                            """
                            CREATE TABLE IF NOT EXISTS tasks 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            title TEXT)
                            """
                            )
        connection.commit()
    finally:
        connection.close()


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

    return None



@app.get("/tasks")
def get_tasks():
    connection = connect_database()
    try:
        tasks = show_tasks(connection)
        
        return tasks
    finally:
        connection.close()


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    connection = connect_database()
    try:
        task = show_task(connection, task_id)
        if task is not None:

            return task

        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    finally:
        connection.close()


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    connection = connect_database()
    try:
        created_task = task.title
        cursor = connection.execute("INSERT INTO tasks (title) VALUES (?)", (created_task,))
        connection.commit()
        task_id = cursor.lastrowid

        return {"id": task_id, "title": created_task}
    finally:
        connection.close()


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    connection = connect_database()
    try:
        updated_task = task_update.title
        if show_task(connection, task_id) is not None:
            connection.execute("UPDATE tasks SET title = ? WHERE id = ?", (updated_task, task_id))
            connection.commit()

            return {"id": task_id, "title": updated_task}

        raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
    finally:
        connection.close()


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    connection = connect_database()
    try:
        task = show_task(connection, task_id)
        if task is not None:
            connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            connection.commit()

            return task

        raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
    finally:
        connection.close()
