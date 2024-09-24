import requests
import shutil
import get_token
import json
import get_image
token=get_token.get_token()
img_json=get_image.get_image("сапог")
img_id = img_json.json()["choices"]["message"]
print (img_id)
# print (img_json.text)

# url = "https://gigachat.devices.sberbank.ru/api/v1/files/92e976c0-ab26-4e64-aae1-1c08467019fd/content"

# headers = {
#   'Accept': 'application/jpg',
#   'Authorization': f'Bearer {token}'
# }

# response = requests.request("GET", url, headers=headers, stream=True, verify=False)
# # print (response.text)
# with open('file.jpg', 'wb') as out_file:
#     shutil.copyfileobj(response.raw, out_file)
# del response