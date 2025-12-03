import requests
import subprocess
import datetime
import time

channel = ""
token = ""
outputFolder = ""
streamlink = ""
webhookurl = ""
headers = {
    "Authorization": f"Bearer {token}",
    "Client-Id": ""
}
user_id = requests.get(f"https://api.twitch.tv/helix/users?login={channel}", headers=headers).json()["data"][0]["id"]

while True:
    response = requests.get(f"https://api.twitch.tv/helix/streams?user_login={channel}", headers=headers).json()
    if (response.get("data")):
        dateLong = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        title = response["data"][0]["title"]
        vodID = requests.get(f"https://api.twitch.tv/helix/videos?user_id={user_id}&type=archive&first=1", headers=headers).json()["data"][0]["id"]

        response = requests.post(
        f"{webhookurl}?wait=true",
        json={"content": f"""
{channel} went live on Twitch on {datetime.datetime.now().strftime("%m-%d-%Y")}
Title: {title}
VOD ID: {vodID}
Start Time: {datetime.datetime.now().strftime("%H-%M-%S")}
End Time: Waiting, Stream in progress...
        """}
        )

        subprocess.run([
            streamlink,
            "--hls-live-restart",
            "--retry-streams", "1",
            "--twitch-api-header", f"Authorization=Bearer {token}",
            "--twitch-disable-hosting",
            "--twitch-low-latency",
            "--stream-segment-threads", "10",
            "--ffmpeg-audio-transcode", "copy",
            "--ffmpeg-video-transcode", "copy",
            f"https://www.twitch.tv/{channel}",
            "best",
            "-o", output_file
        ])
        
        requests.patch(
    f"{webhookurl}/messages/{response.json()['id']}",
    json={"content": f"""
{channel} went live on Twitch on {datetime.datetime.now().strftime("%m-%d-%Y")}
Title: {title}
VOD ID: {vodID}
Start Time: {datetime.datetime.now().strftime("%H-%M-%S")}
End Time: {datetime.datetime.now().strftime("%m-%d-%y %I:%M:%S %p")}
"""})   
    time.sleep(1)