import pytest

from github_repo_reporter import create_repository_report, get_repository_response, input_repository_name

import github_repo_reporter


@pytest.fixture
def valid_data():
    repository_data = {
        "name": "test-repo",
        "full_name": "user/test-repo",
        "description": "Тестовый репозиторий",
        "language": "Python",
        "stargazers_count": 10,
        "forks_count": 3,
        "open_issues_count": 2,
        "updated_at": "2026-08-01T12:30:45Z"
    }
    return repository_data


def test_create_repository_report(valid_data):
    assert create_repository_report(valid_data) == """Название: test-repo
Полное имя: user/test-repo
Описание: Тестовый репозиторий
Основной язык: Python
Количество звёзд: 10
Количество форков: 3
Количество открытых задач: 2
Последнее обновление: 01.08.2026 12:30:45"""


def test_create_repository_report_with_none_description_and_language(valid_data):
    valid_data["description"] = None
    valid_data["language"] = None
    assert create_repository_report(valid_data) == """Название: test-repo
Полное имя: user/test-repo
Описание отсутствует
Основной язык не определён
Количество звёзд: 10
Количество форков: 3
Количество открытых задач: 2
Последнее обновление: 01.08.2026 12:30:45"""


def test_get_repository_response(monkeypatch):
    fake_response = object()

    def fake_get(url, timeout):
        assert url == "https://api.github.com/repos/user/test-repo"
        assert timeout == 10
        return fake_response

    monkeypatch.setattr(
        github_repo_reporter.requests,
        "get",
        fake_get
    )

    result = get_repository_response("user/test-repo")
   

    assert result is fake_response


def test_get_repository_response_timeout(monkeypatch, capsys):
    def fake_get(url, timeout):
        raise github_repo_reporter.requests.Timeout

    monkeypatch.setattr(
        github_repo_reporter.requests,
        "get",
        fake_get
    )

    get_repository_response("user/test-repo")
    captured = capsys.readouterr()

    assert captured.out == "Превышено время ожидания\n"


def test_get_repository_response_request_exception(monkeypatch, capsys):
    def fake_get(url, timeout):
        raise github_repo_reporter.requests.RequestException

    monkeypatch.setattr(
        github_repo_reporter.requests,
        "get",
        fake_get
    )

    get_repository_response("user/test-repo")
    captured = capsys.readouterr()

    assert captured.out == "Ошибка соединения\n"


def test_input_repository_name(monkeypatch):
    def fake_input(prompt):
        return " user/test-repo "
    
    monkeypatch.setattr(
        "builtins.input",
        fake_input
    )

    assert input_repository_name() == "user/test-repo"


def test_input_empty_repository_name(monkeypatch, capsys):
    answers = iter(["  ", "user/test-repo"])
    
    def fake_input(prompt):
        return next(answers)

    monkeypatch.setattr(
        "builtins.input",
        fake_input
    )

    result = input_repository_name()
    captured = capsys.readouterr()

    assert captured.out == "Введен пустой текст\n"
    assert result == "user/test-repo"
