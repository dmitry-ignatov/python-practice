import requests
from datetime import datetime


def get_repository_response(repo_full_name):
    response = requests.get(
        f"https://api.github.com/repos/{repo_full_name}",
        timeout=10
    )

    return response


result = get_repository_response("psf/requests")
if result.status_code == 200:
    repository_data = result.json()
    print(f"Название: {repository_data['name']}")
    print(f"Полное имя: {repository_data['full_name']}")
    print(f"Описание: {repository_data['description']}")
    print(f"Основной язык: {repository_data['language']}")
    print(f"Количество звёзд: {repository_data['stargazers_count']}")
    print(f"Количество форков: {repository_data['forks_count']}")
    print(f"Количество открытых задач: {repository_data['open_issues_count']}")
    date_time = datetime.strptime(repository_data['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
    format_datetime = datetime.strftime(date_time, "%d.%m.%Y %H:%M:%S")
    print(f"Последнее обновление: {format_datetime}")

else:
    print(f"Код ошибки {result.status_code}")