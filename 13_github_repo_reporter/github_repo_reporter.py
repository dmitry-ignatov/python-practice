import requests
from datetime import datetime
from pathlib import Path


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


def create_repository_report(repository_data):
    repository_report = [f"Название: {repository_data['name']}", 
                         f"Полное имя: {repository_data['full_name']}"
                    ]
    if repository_data['description'] is None:
        repository_report.append("Описание отсутствует")
    else:
        repository_report.append(f"Описание: {repository_data['description']}")
    if repository_data['language'] is None:
        repository_report.append("Основной язык не определён")
    else:
        repository_report.append(f"Основной язык: {repository_data['language']}")
    repository_report.append(f"Количество звёзд: {repository_data['stargazers_count']}")
    repository_report.append(f"Количество форков: {repository_data['forks_count']}")
    repository_report.append(f"Количество открытых задач: {repository_data['open_issues_count']}")
    date_time = datetime.strptime(repository_data['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
    formatted_datetime = date_time.strftime("%d.%m.%Y %H:%M:%S")
    repository_report.append(f"Последнее обновление: {formatted_datetime}")

    return "\n".join(repository_report)


def save_repository_report(repository_report):
    try:
        path_for_save_file = Path(__file__).resolve().parent / "repository_report.txt"
        with open(path_for_save_file, "w", encoding="utf-8") as file:
            file.write(repository_report)
        print(f"Отчёт сохранен в: {path_for_save_file}")
    except PermissionError:
        print("Доступ к файлу запрещён")
    except OSError:
        print("Не удалось сохранить отчёт")


def show_repository_report(repository_report):
    print(repository_report)


def main():
    repo_name = input_repository_name()
    result = get_repository_response(repo_name)
    if result is not None:
        if result.status_code == 200:
            repository_data = result.json()
            repository_report = create_repository_report(repository_data)
            show_repository_report(repository_report)
            save_repository_report(repository_report)
        elif result.status_code == 404:
            print("Репозиторий не найден")
        else:
            print(f"Код ошибки: {result.status_code}")


if __name__ == "__main__":
    main()