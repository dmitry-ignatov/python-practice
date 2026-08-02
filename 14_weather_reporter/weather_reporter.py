import requests



def get_city_name():
    city_name = input("Введите название города: ")
    city_name_notmalize = city_name.strip()
    return city_name_notmalize

def get_response(city_name):
    params = {
        "name": city_name,
        "count": 1,
        "language": "ru",
        "format": "json"
    }
    response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params=params,
        timeout=10
    )

    return response


def create_report(response):
    response_json = response.json()
    report = [response_json["results"][0]["name"], response_json["results"][0]["country"], 
              str(response_json["results"][0]["latitude"]), str(response_json["results"][0]["longitude"])

    ]

    return report


def show_report(report):
    print("\n".join(report))



city_name = get_city_name()
response = get_response(city_name)
report = create_report(response)
show_report(report)