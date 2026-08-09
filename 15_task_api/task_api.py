from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Task API"}


tasks = [
    {"id": 1, "title": "Купить хлеб"},
    {"id": 2, "title": "Выучить FastAPI"}
]


@app.get("/tasks")
def get_tasks(task_id: int):
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