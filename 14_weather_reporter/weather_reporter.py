import requests

from pathlib import Path


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
        if "results" not in location_response.json():
             print("Города с таким названием нет")
             return None
        else:
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
    

def get_weather_conditions(forecast_response):
    forecast_response_json = forecast_response.json()
    weather_code = forecast_response_json["current"]["weather_code"]
    if weather_code == 0:
        return "ясно"
    elif weather_code == 1:
        return "преимущественно ясно"
    elif weather_code == 2:
        return "переменная облачность"
    elif weather_code == 3:
        return "пасмурно"
    elif weather_code == 45:
        return "туман"
    elif weather_code == 48:
        return "туман с изморозью"
    elif weather_code == 51:
        return "слабая морось"
    elif weather_code == 53:
        return "умеренная морось"
    elif weather_code == 55:
        return "сильная морось"
    elif weather_code == 56:
        return "слабая ледяная морось"
    elif weather_code == 57:
        return "сильная ледяная морось"
    elif weather_code == 61:
        return "слабый дождь"
    elif weather_code == 63:
        return "умеренный дождь"
    elif weather_code == 65:
        return "сильный дождь"
    elif weather_code == 66:
        return "слабый ледяной дождь"
    elif weather_code == 67:
        return "сильный ледяной дождь"
    elif weather_code == 71:
        return "слабый снег"
    elif weather_code == 73:
        return "умеренный снег"
    elif weather_code == 75:
        return "сильный снег"
    elif weather_code == 77:
        return "снежная крупа"
    elif weather_code == 80:
        return "слабый ливень"
    elif weather_code == 81:
        return "умеренный ливень"
    elif weather_code == 82:
        return "сильный ливень"
    elif weather_code == 85:
        return "слабый снежный ливень"
    elif weather_code == 86:
        return "сильный снежный ливень"
    elif weather_code == 95:
        return "гроза"
    elif weather_code == 96:
        return "гроза со слабым градом"
    elif weather_code == 99:
        return "гроза с сильным градом"
    else:
        return "Неизвестное погодное состояние"


def create_technical_report(location_response, forecast_response):
    location_response_json = location_response.json()
    forecast_response_json = forecast_response.json()
    weather_conditions = get_weather_conditions(forecast_response)

    technical_report = [
        location_response_json["results"][0]["name"], 
        location_response_json["results"][0]["country"], 
    str(location_response_json["results"][0]["latitude"]), 
    str(location_response_json["results"][0]["longitude"]),

        forecast_response_json["current"]["temperature_2m"],
        forecast_response_json["current"]["apparent_temperature"],
        weather_conditions,
        forecast_response_json["current"]["wind_speed_10m"],

        forecast_response_json["daily"]["time"],
        forecast_response_json["daily"]["temperature_2m_min"],
        forecast_response_json["daily"]["temperature_2m_max"],
        forecast_response_json["daily"]["precipitation_probability_max"],
    ]

    return technical_report


def create_report(technical_report):
    
    report = [
        f"Название города: {technical_report[0]}",
        f"Страна: {technical_report[1]}",
        f"Ширина: {technical_report[2]}",
        f"Долгота: {technical_report[3]}\n",

        f"Текущаяя погода:\n\nТемпература: {technical_report[4]} °C",
        f"Ощущается как: {technical_report[5]} °C",
        f"Состояние: {technical_report[6]}",
        f"Скорость ветра: {technical_report[7]} km/h\n",

        f"Прогноз на 3 дня\n\nДата: {technical_report[8][0]}",
        f"Минимальная температура: {technical_report[9][0]} °C",
        f"Максимальная температура: {technical_report[10][0]} °C",
        f"Вероятность осадков: {technical_report[11][0]} %\n",

        f"Дата: {technical_report[8][1]}",
        f"Минимальная температура: {technical_report[9][1]} °C",
        f"Максимальная температура: {technical_report[10][1]} °C",
        f"Вероятность осадков: {technical_report[11][1]} %\n",

        f"Дата: {technical_report[8][2]}",
        f"Минимальная температура: {technical_report[9][2]} °C",
        f"Максимальная температура: {technical_report[10][2]} °C",
        f"Вероятность осадков: {technical_report[11][2]} %\n",
    ]

    return report


def show_report(report):
    print("\n".join(report))


def save_report(report, location_response):
    path = Path(__file__).parent.resolve() / f"{location_response.json()["results"][0]["name"]}_weather_report.txt"
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write("\n".join(report))
        print(f"Отчет сохранен в: {path}")
    except PermissionError:
        print("Нет доступа к файлу")
    except OSError:
        print("Не удалось сохранить отчёт")


def main():
    city_name = get_city_name()
    location_response = get_location_response(city_name)
    if location_response is not None:
        forecast_response = get_forecast_response(location_response)
        if forecast_response is not None:
            technical_report = create_technical_report(location_response, forecast_response)
            report = create_report(technical_report)
            show_report(report)
            save_report(report, location_response)


if __name__ == "__main__":
    main()