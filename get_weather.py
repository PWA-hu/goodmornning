import openweathermapapi

# weather = ""


def get_weather():
    data_json = openweathermapapi.weatherjson()
    weather = (
        "Погода в городе "
        + data_json["name"]
        + ":\n"
        + data_json["weather"][int(0)]["description"]
        + "\nТемпература воздуха - "
        + str(data_json["main"]["temp"])
        + "\nАтмосферное давление - "
        + str(data_json["main"]["pressure"])
        + "\nСкорость ветра - "
        + str(data_json["wind"]["speed"])
    )
    return weather


