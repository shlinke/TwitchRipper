import requests
import subprocess
import datetime
import time

channel = ""
Token = ""
outputFolder = ""
streamlink = ""

headers = {
    "Authorization": f"Bearer {Token}",
    "Client-Id": ""
}
user_id = requests.get(f"https://api.twitch.tv/helix/users?login={channel}", headers=headers).json()["data"][0]["id"]

while True:
    response = requests.get(f"https://api.twitch.tv/helix/streams?user_login={channel}", headers=headers).json()
    if (response.get("data")):
        dateLong = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        subprocess.run([streamlink])
    time.sleep(1)