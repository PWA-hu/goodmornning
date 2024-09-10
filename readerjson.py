import json

# открыть файл
def parsjson(name_field):
    with open(".e.json") as readfile:
        datajson = json.load(readfile)
    return datajson[name_field]