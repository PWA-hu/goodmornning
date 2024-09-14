import requests
import readerjson
import text
# from prettytable import PrettyTable
# api openweathermap.org/
# получить текующие погодные условия от сервиса
def weatherjson():

    city = text.city
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

# получить прогноз погоды от сервиса
def weatherjson_forecst():

    city = text.city
    city_id = 0
    appid = readerjson.parsjson("weather_token")
    h_forecast = (
        "https://ru.api.openweathermap.org/data/2.5/forecast?q="
        + city
        + "&lang=ru"
        + "&units=metric"
        + "&appid="
        + appid
    )
    print ( h_forecast )
    response = requests.get(h_forecast)
    # print(response.status_code)
    # print(response.json())
    return response.json()