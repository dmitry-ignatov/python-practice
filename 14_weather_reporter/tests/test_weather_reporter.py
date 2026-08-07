import pytest

from weather_reporter import get_city_name, get_location_response, get_forecast_response
import weather_reporter


# @pytest.fixture
# def valid_data(city_name):
#     params = {
#         "name": "Ryazan",
#         "count": 1,
#         "language": "ru",
#         "format": "json"
#     }

#     return params


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
        return fake_response

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    result = get_location_response("Ryazan")

    assert result == fake_response.json()


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


def test_get_forecast_response(monkeypatch):
    fake_forecast_response = FakeResponse(200, {})
    fake_location_response = {
                    "results": [
                                    {
                                    "latitude": 54.6,
                                    "longitude": 39.7
                                    }
                               ]
                }

    def fake_get_response(url, params, timeout):
        return fake_forecast_response

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    result = get_forecast_response(fake_location_response)

    assert result == fake_forecast_response.json()


def test_get_forecast_response_error(monkeypatch, capsys):
    fake_forecast_response = FakeResponse(404, {})
    fake_location_response = {
                    "results": [
                                    {
                                    "latitude": 54.6,
                                    "longitude": 39.7
                                    }
                                ]
                }

    def fake_get_response(url, params, timeout):
        return fake_forecast_response

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    get_forecast_response(fake_location_response)
    captured = capsys.readouterr()

    assert captured.out == "Ошибка запроса\n"


