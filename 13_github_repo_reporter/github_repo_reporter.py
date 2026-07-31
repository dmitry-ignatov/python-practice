import requests
from datetime import datetime


def input_repository_name():
    while True:
        repo_name = input("Введите название репозитория в формате владелец/репозиторий: ")
        normalized_repo_name = repo_name.strip()
        if not normalized_repo_name:
            print("Введен пустой текст")
        else:
            repo_name_parts = normalized_repo_name.split("/")
            if len(repo_name_parts) != 2:
                print("Введен неверный формат")
            elif "" in repo_name_parts or any(char.isspace() for part in repo_name_parts for char in part):
                print("Введен неверный формат")
            else:
                return normalized_repo_name


def get_repository_response(repo_full_name):
    try:
        response = requests.get(
            f"https://api.github.com/repos/{repo_full_name}",
            timeout=10
        )

        return response
    except requests.Timeout:
        print("Превышено время ожидания")
        return
    except requests.RequestException:
        print("Ошибка соединения")
        return


repo_name = input_repository_name()
result = get_repository_response(repo_name)
if result is not None:
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
        formatted_datetime = date_time.strftime("%d.%m.%Y %H:%M:%S")
        print(f"Последнее обновление: {formatted_datetime}")
    elif result.status_code == 404:
        print("Репозиторий не найден")
    else:
        print(f"Код ошибки: {result.status_code}")