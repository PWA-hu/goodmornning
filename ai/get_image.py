import requests
import get_token
import apisecretgiga
import json

# giga_access_token = get_token.get_token(apisecretgiga.auth)
giga_access_token = get_token.get_token()
# получить ответ со ссылкой на изображение
def get_image(message):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {giga_access_token}",
    }
    payload = {
  "model": "GigaChat:latest",
  "messages": [
    {
      "role": "system",
      "content": "Ты — Василий Кандинский"      
    },
    {
      "role": "user",
      "content": message
    }
  ],
  "function_call": "auto"
}

    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    return response

#  получить список моделей
def get_models():
    url = "https://gigachat.devices.sberbank.ru/api/v1/models"
    payload = {}
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {giga_access_token}",
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return response.text
