import json
import requests
headers = {"Authorization": "Bearer --TOKEN--"}
para = {
    "name": "--FILE--",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./--FILE--", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)