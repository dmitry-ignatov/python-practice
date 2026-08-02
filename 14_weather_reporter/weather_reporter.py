import requests



def get_city_name():
    while True:
        city_name = input("Введите название города: ")
        city_name_notmalize = city_name.strip()
        if not city_name_notmalize:
            print("Введена пустой текст")
        else:
            print()
            return city_name_notmalize


def get_location_response(city_name):
    params = {
        "name": city_name,
        "count": 1,
        "language": "ru",
        "format": "json"
    }
    try:
        location_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params=params,
            timeout=10
        )

        return location_response
    
    except requests.Timeout:
        print("Превышено время ожидания")
    except requests.RequestException:
        print("Ошибка соединения")


def get_forecast_response(location_response):
    location_response_json = location_response.json()
    params = {
        "latitude": location_response_json["results"][0]["latitude"],
        "longitude": location_response_json["results"][0]["longitude"],
        "current": (
            "temperature_2m,"
            "apparent_temperature,"
            "weather_code,"
            "wind_speed_10m"
        ),
        "daily": (
            "weather_code,"
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_probability_max"
        ),
        "timezone": "auto",
        "forecast_days": 3
    }

    try:
        forecast_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params=params,
            timeout=10
        )

        return forecast_response
    
    except requests.Timeout:
        print("Превышено время ожидания")
    except requests.RequestException:
        print("Ошибка соединения")


def create_report(location_response, forecast_response):
    location_response_json = location_response.json()
    forecast_response_json = forecast_response.json()
    try:
        report = [location_response_json["results"][0]["name"], 
                  location_response_json["results"][0]["country"], 
              str(location_response_json["results"][0]["latitude"]), 
              str(location_response_json["results"][0]["longitude"]),

              forecast_response_json["current"]["temperature_2m"],
              forecast_response_json["current"]["apparent_temperature"],
              forecast_response_json["current"]["weather_code"],
              forecast_response_json["current"]["wind_speed_10m"],

              forecast_response_json["daily"]["time"],
              forecast_response_json["daily"]["temperature_2m_min"],
              forecast_response_json["daily"]["temperature_2m_max"],
              forecast_response_json["daily"]["precipitation_probability_max"],

        ]

        return report
    except KeyError:
        print("Города с таким названием нет")


def show_report(report):
    print(f"""Название города: {report[0]}
Страна: {report[1]}
Ширина: {report[2]}
Долгота: {report[3]}

Текущаяя погода:
Температура: {report[4]} °C
Ощущается как: {report[5]} °C
{report[6]}
Скорость ветра: {report[7]} km/h

Прогноз на 3 дня

Дата: {report[8][0]}
Минимальная температура: {report[9][0]} °C
Максимальная температура: {report[10][0]} °C
Вероятность осадков: {report[11][0]} %

Дата: {report[8][1]}
Минимальная температура: {report[9][1]} °C
Максимальная температура: {report[10][1]} °C
Вероятность осадков: {report[11][1]} %

Дата: {report[8][2]}
Минимальная температура: {report[9][2]} °C
Максимальная температура: {report[10][2]} °C
Вероятность осадков: {report[11][2]} %
""")



city_name = get_city_name()
location_response = get_location_response(city_name)
forecast_response = get_forecast_response(location_response)
if location_response is not None:
    report = create_report(location_response, forecast_response)
if report is not None:
    show_report(report)