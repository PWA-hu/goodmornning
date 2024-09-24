import uuid
import requests
import apisecretgiga

def get_token():
    auth = apisecretgiga.auth
    rq_id = str(uuid.uuid4())
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    payload = "scope=GIGACHAT_API_PERS"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": rq_id,
        "Authorization": f"Basic {auth}",
    }
    try:
      response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False
      )
      token_giga = response.json()['access_token']
      return token_giga
    except requests.RequestException as e:
      print (e)
      return -1
    