import os

import requests

BASE_URL = os.environ["PRTIMES_URL"]
ACCESS_TOKEN = os.environ["PRTIMES_API_KEY"]
url = BASE_URL + "/releases"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}",
}
res = requests.get(url, headers=headers)

print(res.json())
