from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str



@app.get("/")
def root():
    return {"message": "Task API"}


tasks = [
    {"id": 1, "title": "Купить хлеб"},
    {"id": 2, "title": "Выучить FastAPI"}
]


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task_id == task["id"]:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    if tasks:
        created_task = {
            "id": tasks[-1]["id"] + 1, "title": task.title
        }
    else:
        created_task = {
            "id": 1, "title": task.title
        }

    tasks.append(created_task)
    return created_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task_id == task["id"]:
            tasks.remove(task)
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task_id == task["id"]:
            task["title"] = task_update.title
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )