import threading
import os
import requests
import subprocess
import datetime
import time

streamlink = r"" # https://streamlink.github.io/install.html
ffmpeg = r"" # https://www.ffmpeg.org/download.html
twitchdownloadercli = r"" # https://github.com/lay295/TwitchDownloader

channel = ""
outputFolder = r""
token = "" # Get Twitch AUTH token from https://twitchtokengenerator.com/ this will expire after some time so make sure to update it when needed
webhookurl = "" # Discord webhook URL
headers = {
    "Authorization": f"Bearer {token}",
    "Client-Id": "gp762nuuoqcoxypju8c569th9wz7q5" # Public Client ID from https://twitchtokengenerator.com/
}
user_id = requests.get(f"https://api.twitch.tv/helix/users?login={channel}", headers=headers).json()["data"][0]["id"]

while True:
    response = requests.get(f"https://api.twitch.tv/helix/streams?user_login={channel}", headers=headers).json()
    
    if response.get("data"):
        dateLong = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        title = response["data"][0]["title"]
        vodID = requests.get(f"https://api.twitch.tv/helix/videos?user_id={user_id}&type=archive&first=1", headers=headers).json()["data"][0]["id"]
        outputfile = os.path.join(outputFolder, f"[{dateLong}] {vodID} broadcast.ts")

        discordresponse = requests.post(
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
            "-o", outputfile
        ])
        
        requests.patch(
            f"{webhookurl}/messages/{discordresponse.json()['id']}",
            json={"content": f"""
{channel} went live on Twitch on {datetime.datetime.now().strftime("%m-%d-%Y")}
Title: {title}
VOD ID: {vodID}
Start Time: {datetime.datetime.now().strftime("%H-%M-%S")}
End Time: {datetime.datetime.now().strftime("%m-%d-%y %I:%M:%S %p")}
            """}
        )

        threading.Thread(
            target=lambda: (
                subprocess.Popen(
                    [twitchdownloadercli, "chatdownload", "--id", vodID, "--collision", "Rename", "-E",
                     "--output", os.path.join(outputFolder, f"[{dateLong}] {vodID}.json")],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                ),
                subprocess.run(
                    [twitchdownloadercli, "videodownload", "--id", vodID, "--collision", "Rename",
                     "--quality", "best", "--threads", "16",
                     "--output", os.path.join(outputFolder, f"[{dateLong}] {vodID} vod.mp4")],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                ),
                subprocess.Popen([
                    "ffmpeg", "-threads", "16",
                    "-i", os.path.join(outputFolder, f"[{dateLong}] {vodID} vod.mp4"),
                    "-i", outputfile,
                    "-map", "0:v", "-map", "1:a", "-map", "0:a",
                    "-metadata:s:a:0", "title=Broadcast Audio",
                    "-metadata:s:a:1", "title=VOD Audio",
                    "-disposition:a:0", "default",
                    "-disposition:a:1", "none",
                    "-c:v", "copy", "-c:a", "copy",
                    "-fflags", "+genpts", "-avoid_negative_ts", "make_zero",
                    "-shortest",
                    f"{vodID} [{dateLong}].mkv"
                ]),
                print(f"Finished post processing for {vodID}")
            ),
            daemon=True
        ).start()

    time.sleep(1)
