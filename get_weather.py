import openweathermapapi


# weather = ""


# получить погоду в заданном по умолчанию городе
def get_weather_on_line():
    # подгрузить погоду в переменную data_json
    data_json = openweathermapapi.weatherjson()
    # иконка погоды
    # response = requests.get("http://openweathermap.org/img/w/01n.png")
    # img_data = response.content
    # image = Image.open(BytesIO(img_data))
    # image.show()
    # --------
    # data_json = openweathermapapi.weatherjson()
    weather = (
        "Погода в городе "
        + data_json["name"]
        + "\n"
        + data_json["weather"][int(0)]["description"]
        + "\nТемпература воздуха - "
        + str(data_json["main"]["temp"])
        + "\nАтмосферное давление - "
        + str(data_json["main"]["pressure"])
        + "\nСкорость ветра - "
        + str(data_json["wind"]["speed"])
    )
    return weather

    # table = PrettyTable()
    # table.field_names = ["01", ""]

    # table.add_rows(
    #     [
    #         ["температура воздуха", data_json["weather"][int(0)]["description"]],
    #         ["Атмосферное давление", str(data_json["main"]["pressure"])],
    #         ["Скорость ветра", str(data_json["wind"]["speed"])],
    #         # ["Hobart", 1357, 205556, 619.5],
    #         # ["Sydney", 2058, 4336374, 1214.8],
    #         # ["Melbourne", 1566, 3806092, 646.9],
    #         # ["Perth", 5386, 1554769, 869.4],
    #     ]
    # )
 
    # return table


# получить прогноз погоды
def get_weather_forecast():
    data_json = openweathermapapi.weatherjson_forecst()
    weather_forecast = "прогноз погоды на   дней в городе" + data_json["name"] + "\n"
    return weather_forecast
