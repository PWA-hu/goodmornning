import openweathermapapi
temp = "температура воздуха в аксае: " + str(openweathermapapi.weatherjson())
print(temp)