import pytest

from weather_reporter import get_city_name, get_location_response
import weather_reporter


@pytest.fixture
def valid_data(city_name):
    params = {
        "name": "Ryazan",
        "count": 1,
        "language": "ru",
        "format": "json"
    }

    return params


class FakeResponse:

    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data


def test_input_city_name(monkeypatch):
    def fake_input(prompt):
        return "  Ryazan  "

    monkeypatch.setattr(
        "builtins.input",
        fake_input
    )

    assert get_city_name() == "Ryazan"


def test_input_empty_city_name(monkeypatch, capsys):
    answers = iter([" ", "Ryazan"])

    def fake_input(prompt):
        return next(answers)

    monkeypatch.setattr(
        "builtins.input",
        fake_input
    )

    result = get_city_name()
    captured = capsys.readouterr()

    assert captured.out == "Введен пустой текст\n\n"
    assert result == "Ryazan"


def test_get_location_response(monkeypatch):
    
    fake_response = FakeResponse(200, 
                {
                    "results": [
                                    {
                                    "latitude": 54.6,
                                    "longitude": 39.7
                                    }
                                ]
                }
            )

    def fake_get_response(url, params, timeout):
        assert url == "https://geocoding-api.open-meteo.com/v1/search"
        assert params == params
        assert timeout == 10
        
        return fake_response

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    result = get_location_response("Ryazan")

    assert result is fake_response


def test_get_empty_location_response(monkeypatch,capsys):
    fake_response = FakeResponse(200, {"results": []})
    def fake_get_response(url, params, timeout):
        return fake_response

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    get_location_response("Ryazan")
    captured = capsys.readouterr()
    
    assert captured.out == "Города с таким названием нет\n"


def test_get_location_response_timout(monkeypatch,capsys):
    fake_response =  object()
    def fake_get_response(url, params, timeout):
        raise weather_reporter.requests.Timeout

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )
    get_location_response("Ryazan")
    captured = capsys.readouterr()

    assert captured.out == "Превышено время ожидания\n"