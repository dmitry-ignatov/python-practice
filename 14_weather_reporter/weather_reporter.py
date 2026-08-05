import requests
from pathlib import Path
from datetime import datetime


def get_city_name():
    while True:
        city_name = input("Введите название города: ")
        city_name_normalize = city_name.strip()
        if not city_name_normalize:
            print("Введен пустой текст")
        else:
            print()
            return city_name_normalize


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
        if location_response.status_code == 200: 
            if "results" not in location_response.json() or location_response.json()["results"] == []:
                print("Города с таким названием нет")
                return None
            else:
                return location_response
        else:
            print("Ошибка запроса")
    
    except requests.Timeout:
        print("Превышено время ожидания")
    except requests.RequestException:
        print("Ошибка соединения")


def get_json_format(location_response, forecast_response):
    json_data_format = {
                        "location_response": "",
                        "forecast_response": ""
                        }
    if location_response is not None:
        json_data_format["location_response"] = location_response.json()
    if forecast_response is not None:
        json_data_format["forecast_response"] = forecast_response.json()

    return json_data_format


def get_forecast_response(location_response):
    json_data_format = get_json_format(location_response, None)
    params = {
        "latitude": json_data_format["location_response"]["results"][0]["latitude"],
        "longitude": json_data_format["location_response"]["results"][0]["longitude"],
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
        if forecast_response.status_code == 200:
            return forecast_response
        else:
            print("Ошибка запроса")

    except requests.Timeout:
        print("Превышено время ожидания")
    except requests.RequestException:
        print("Ошибка соединения")
    

def get_weather_conditions(forecast_response, prompt):
    json_data_format = get_json_format(None, forecast_response)
    weathers = []

    if prompt == "current":
        weather_code = [str(json_data_format["forecast_response"]["current"]["weather_code"])]
    elif prompt == "daily":
        weather_code_int = json_data_format["forecast_response"]["daily"]["weather_code"]
        weather_code = [str(code) for code in weather_code_int]
    for code in weather_code:
        if code == "0":
            weathers.append("ясно")
        elif code == "1":
            weathers.append("преимущественно ясно")
        elif code == "2":
            weathers.append("переменная облачность")
        elif code == "3":
            weathers.append("пасмурно")
        elif code == "45":
            weathers.append("туман")
        elif code == "48":
            weathers.append("туман с изморозью")
        elif code == "51":
            weathers.append("слабая морось")
        elif code == "53":
            weathers.append("умеренная морось")
        elif code == "55":
            weathers.append("сильная морось")
        elif code == "56":
            weathers.append("слабая ледяная морось")
        elif code == "57":
            weathers.append("сильная ледяная морось")
        elif code == "61":
            weathers.append("слабый дождь")
        elif code == "63":
            weathers.append("умеренный дождь")
        elif code == "65":
            weathers.append("сильный дождь")
        elif code == "66":
            weathers.append("слабый ледяной дождь")
        elif code == "67":
            weathers.append("сильный ледяной дождь")
        elif code == "71":
            weathers.append("слабый снег")
        elif code == "73":
            weathers.append("умеренный снег")
        elif code == "75":
            weathers.append("сильный снег")
        elif code == "77":
            weathers.append("снежная крупа")
        elif code == "80":
            weathers.append("слабый ливень")
        elif code == "81":
            weathers.append("умеренный ливень")
        elif code == "82":
            weathers.append("сильный ливень")
        elif code == "85":
            weathers.append("слабый снежный ливень")
        elif code == "86":
            weathers.append("сильный снежный ливень")
        elif code == "95":
            weathers.append("гроза")
        elif code == "96":
            weathers.append("гроза со слабым градом")
        elif code == "99":
            weathers.append("гроза с сильным градом")
        else:
            weathers.append("неизвестное погодное состояние")

    return weathers

def get_current_time(forecast_response):
    json_data_format = get_json_format(None, forecast_response)
    date_time = datetime.strptime(json_data_format["forecast_response"]["current"]["time"], "%Y-%m-%dT%H:%M")
    date_time = datetime.strftime(date_time, "%Y-%m-%d %H:%M")
    return date_time


def create_technical_report(location_response, forecast_response):
    json_data_format = get_json_format(location_response, forecast_response)
    weather_conditions_current = get_weather_conditions(forecast_response, "current")
    weather_conditions_daily = get_weather_conditions(forecast_response, "daily")
    date_time = get_current_time(forecast_response)

    technical_report = {
        "name": json_data_format["location_response"]["results"][0]["name"], 
        "country": json_data_format["location_response"]["results"][0]["country"], 
        "latitude": str(json_data_format["location_response"]["results"][0]["latitude"]), 
        "longitude": str(json_data_format["location_response"]["results"][0]["longitude"]),

        "date time": date_time,
        "temperature": json_data_format["forecast_response"]["current"]["temperature_2m"],
        "apparent temperature": json_data_format["forecast_response"]["current"]["apparent_temperature"],
        "current weather conditions": weather_conditions_current[0],
        "wind speed": json_data_format["forecast_response"]["current"]["wind_speed_10m"],

        "time": json_data_format["forecast_response"]["daily"]["time"],
        "daily weather conditions": weather_conditions_daily,
        "temperature min": json_data_format["forecast_response"]["daily"]["temperature_2m_min"],
        "temperature max": json_data_format["forecast_response"]["daily"]["temperature_2m_max"],
        "precipitation probability": json_data_format["forecast_response"]["daily"]["precipitation_probability_max"],
    }

    return technical_report


def get_3day_forecast(technical_report, day_index):
    return f"""Дата: {technical_report["time"][day_index]}
Состояние: {technical_report["daily weather conditions"][day_index]}
Минимальная температура: {technical_report["temperature min"][day_index]} °C
Максимальная температура: {technical_report["temperature max"][day_index]} °C
Вероятность осадков: {technical_report["precipitation probability"][day_index]} %\n"""


def create_report(technical_report):
    
    report = [
        f"Название города: {technical_report["name"]}",
        f"Страна: {technical_report["country"]}",
        f"Широта: {technical_report["latitude"]}",
        f"Долгота: {technical_report["longitude"]}\n",
        
        "Текущая дата и время: ",
        f"{technical_report["date time"]}",
        f"Текущая погода:\n",
        f"Температура: {technical_report["temperature"]} °C",
        f"Ощущается как: {technical_report["apparent temperature"]} °C",
        f"Состояние: {technical_report["current weather conditions"]}",
        f"Скорость ветра: {technical_report["wind speed"]} km/h\n",

        f"Прогноз на 3 дня\n",
        get_3day_forecast(technical_report, 0),
        get_3day_forecast(technical_report, 1),
        get_3day_forecast(technical_report, 2)
    ]

    return report


def show_report(report):
    print("\n".join(report))


def save_report(report, location_response):
    path = Path(__file__).parent.resolve() / f"{location_response.json()["results"][0]["name"]}_{datetime.now().strftime("%Y.%m.%d_%H-%M")}_weather_report.txt"
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