FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "task_api_sqlite:app", "--host", "0.0.0.0"]