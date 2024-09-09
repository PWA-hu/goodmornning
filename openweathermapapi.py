import requests
import openweathermapapi


# api openweathermap.org/
# получить текующие погодные условия от сервиса
def weatherjson():

    city = "Aksay,ru"
    city_id = 0
    appid = "c29102cc9ef08d1e638e7d91e9e90315"
    h = (
        "https://ru.api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&lang=ru"
        + "&units=metric"
        + "&appid="
        + appid
    )

    response = requests.get(h)
    print(response.status_code)
    data = response.json()
    temperature = data["main"]["temp"]
    return data
