import pytest

from weather_reporter import (get_city_name, get_location_response, 
                              get_forecast_response, get_weather_conditions, 
                              create_technical_report, get_3day_forecast, create_report, 
                              save_report)
import weather_reporter

@pytest.fixture
def location_response_data():
    response_data = {
        "results": 
                    [
                        {       
                            "name": "Рязань", 
                            "country": "Россия", 
                            "latitude": 54.625, 
                            "longitude": 39.6875
                        }
                    ]
    }

    return response_data


@pytest.fixture
def forecast_response_data():
    response_data = {
        "current": 
                    {
                        "time": "2026-08-07T16:45",
                        "temperature_2m": 31.3,
                        "apparent_temperature": 33.0,
                        "weather_code": 3,
                        "wind_speed_10m": 12.3,
                    },

        "daily": 
                    {
                        "time": ['2026-08-07', '2026-08-08', '2026-08-09'],
                        "weather_code": [95, 96, 61],
                        "temperature_2m_min": [20.6, 17.5, 15.0],
                        "temperature_2m_max": [32.2, 25.1, 24.0],
                        "precipitation_probability_max": [28, 50, 35]
                    }
    }

    return response_data


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


def test_get_location_response(monkeypatch, location_response_data):
    
    fake_response = FakeResponse(200, location_response_data)

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


def test_get_location_response_error_code(monkeypatch, capsys):
    fake_response = FakeResponse(404, {})

    def fake_get_response(url, params, timeout):
        return fake_response

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )
    get_location_response("Рязань")
    captured = capsys.readouterr()

    assert captured.out == "Ошибка запроса\n"


def test_get_location_response_timeout(monkeypatch,capsys):
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


def test_get_location_response_Request_exception(monkeypatch,capsys):
    def fake_get_response(url, params, timeout):
        raise weather_reporter.requests.RequestException

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )
    get_location_response("Ryazan")
    captured = capsys.readouterr()

    assert captured.out == "Ошибка соединения\n"


def test_get_forecast_response(monkeypatch, location_response_data):
    fake_forecast_response = FakeResponse(200, {})

    def fake_get_response(url, params, timeout):
        return fake_forecast_response

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    result = get_forecast_response(location_response_data)

    assert result == fake_forecast_response.json()


def test_get_forecast_response_error(monkeypatch, capsys, location_response_data):
    fake_forecast_response = FakeResponse(404, {})

    def fake_get_response(url, params, timeout):
        return fake_forecast_response

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    get_forecast_response(location_response_data)
    captured = capsys.readouterr()

    assert captured.out == "Ошибка запроса\n"


def test_get_forecast_response_timeout(monkeypatch, location_response_data, capsys):
    def fake_get_response(url, params, timeout):
        raise weather_reporter.requests.Timeout

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    get_forecast_response(location_response_data)
    captured = capsys.readouterr()

    assert captured.out == "Превышено время ожидания\n"


def test_get_forecast_response_Request_exception(monkeypatch, location_response_data, capsys):
    def fake_get_response(url, params, timeout):
        raise weather_reporter.requests.RequestException

    monkeypatch.setattr(
        weather_reporter.requests,
        "get",
        fake_get_response
    )

    get_forecast_response(location_response_data)
    captured = capsys.readouterr()

    assert captured.out == "Ошибка соединения\n"


def test_get_weather_conditions_current(forecast_response_data):

    assert get_weather_conditions(forecast_response_data, "current") == ["пасмурно"]


def test_get_weather_conditions_daily(forecast_response_data):

    assert get_weather_conditions(forecast_response_data, "daily") == ["гроза", "гроза со слабым градом", "слабый дождь"]


def test_get_weather_conditions_unknown_condition_current():
    forecast_response = {
        "current": 
                    {
                        "weather_code": 200
                    }
    }
    assert get_weather_conditions(forecast_response, "current") == ["неизвестное погодное состояние"]


def test_get_weather_conditions_unknown_condition_daily():
    forecast_response = {
        "daily": 
                    {
                        "weather_code": [200, 1, 200]
                    }
    }
    assert get_weather_conditions(forecast_response, "daily") == ["неизвестное погодное состояние", "преимущественно ясно", "неизвестное погодное состояние"]


def test_create_technical_report(location_response_data, forecast_response_data):
    current_weather_conditions = get_weather_conditions(forecast_response_data, "current")
    daily_weather_conditions = get_weather_conditions(forecast_response_data, "daily")
    result = create_technical_report(location_response_data, forecast_response_data)

    assert result["name"] == "Рязань"
    assert result["latitude"] == "54.625"
    assert result["date time"] == "2026-08-07 16:45"
    assert result["time"] == ['2026-08-07', '2026-08-08', '2026-08-09']
    assert result["current weather conditions"] == current_weather_conditions[0]
    assert result["temperature max"] == [32.2, 25.1, 24.0]
    assert result["daily weather conditions"] == daily_weather_conditions


def test_create_report():
    technical_report = {
        "name": "Рязань",
        "country": "Россия",
        "latitude": "54.625",
        "longitude": "39.6875",
        "date time": "2026-08-07 16:45",
        "temperature": 31.3,
        "apparent temperature": 33.0,
        "current weather conditions": "пасмурно",
        "time": ['2026-08-07', '2026-08-08', '2026-08-09'],
        "temperature max": [32.2, 25.1, 24.0],
        "temperature min": [20.6, 17.5, 15.0],
        "daily weather conditions": ["гроза", "гроза со слабым градом", "слабый дождь"],
        "wind speed": 12.3,
        "precipitation probability": [28, 50, 35]
    }

    
    result = create_report(technical_report)

    assert result[0] == f"Название города: {technical_report["name"]}"
    assert result[2] == f"Широта: {technical_report["latitude"]}"
    assert result[5] == f"{technical_report["date time"]}\n"
    assert result[12] == get_3day_forecast(technical_report, 0)
    assert result[13] == get_3day_forecast(technical_report, 1)
    assert result[14] == get_3day_forecast(technical_report, 2)


def test_save_report(tmp_path, monkeypatch, location_response_data):
    report = ["test"]

    monkeypatch.setattr(
        weather_reporter,
        "__file__",
        tmp_path / "_weather_report.py"
    )

    save_report(report, location_response_data)
    files = list(tmp_path.glob("Рязань_*_weather_report.txt"))
    assert len(files) == 1
    with open(files[0], "r", encoding="utf-8") as file:
        text = file.read()
    assert text == "\n".join(report)