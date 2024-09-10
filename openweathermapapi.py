import requests


import readerjson


# api openweathermap.org/
# получить текующие погодные условия от сервиса
def weatherjson():

    city = "Aksay,ru"
    city_id = 0
    appid = readerjson.parsjson("weather_token")
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
    return response.json()
