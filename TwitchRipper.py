import requests
import subprocess
import datetime
import time
channel = ""
Token = ""
outputFolder = ""
streamlink = ""

while True:
    headers = {
    "Authorization": f"Bearer {Token}",
    "Client-Id": ""
}

url = f"https://api.twitch.tv/helix/streams?user_login={channel}"
response = requests.get(url, headers=headers).json()
if response.get("data"):
    dateLong = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    subprocess.run([streamlink])
time.sleep(1)