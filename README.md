# TwitchRipper

TwitchRipper is a Python script that automatically downloads Twitch streams, archives VODs, and posts live notifications to Discord.

---

## Features
- Detects when a Twitch channel goes live
- Downloads live streams using Streamlink
- Downloads VODs and chat using TwitchDownloaderCLI
- Merges broadcast and VOD audio with FFmpeg
- Sends notifications and updates to a Discord webhook
- Runs post-processing in a background thread

---

## Dependencies

- Python 3.13+
- [Streamlink](https://streamlink.github.io/)
- [FFmpeg](https://ffmpeg.org/download.html)
- [TwitchDownloaderCLI](https://github.com/lay295/TwitchDownloader)

All Dependencies must be installed and the path linked in the corresponding variable in the script.

---

## How to use

1. Download `TwitchRipper.py` from the repository.
2. Install Python 3.13+ and the required tools:
   - [Streamlink](https://streamlink.github.io/)
   - [FFmpeg](https://ffmpeg.org/download.html)
   - [TwitchDownloaderCLI](https://github.com/lay295/TwitchDownloader)
3. Edit the script variables to configure the channel, Twitch token, output folder, etc.
4
---

## Why TwitchRipper?

TwitchRipper takes all the pros from similar tools like StreamRecorder, TwitchDownloader, and TwitchLink. Only problem is you need alot of storage and a computer running 24/7 (if you have a NAS this is perfect for you). 1h of a 1080p60fps stream is about 2.5GB, this can add up quickly. Below you can see ~35 streams I've archived with this script, this adds up to ~385GB.
<br>
![](https://assets.shlinke.tech/archive.png)
<table>
  <tr>
    <th colspan="3">Comparison of Different Twitch Stream Downloading Tools</th>
  </tr>
  <tr>
    <th>Tool</th>
    <th>Pros</th>
    <th>Cons</th>
  </tr>
  <tr>
    <td>TwitchRipper</td>
    <td>
      - Downloads broadcast and VOD<br>
      - Merges the broadcast and VOD into one .mkv<br>
      - Locally Hosted<br>
      - Downloads chat as JSON automatically<br>
      - Discord notifications for streams<br>
      - No ads (needs sub or proxy)
    </td>
    <td>
      - You're gonna need alot of storage<br>
      (You probably already do if you're archiving Twitch streamers) <br>
      - Needs a computer running 24/7<br>
      - Needs good internet speed<br>
    </td>
  </tr>
  <tr>
    <td>StreamRecorder</td>
    <td>
      - Gets other services than Twitch<br>
      - Records broadcasts<br>
      - Broadcasts become unavalible after 7 days<br> 
    </td>
    <td>
      - Doesn't get VOD<br>
      - $10 a month<br>
      - 720p60fps
    </td>
  </tr>
  <tr>
    <td>TwitchDownloader <br>and<br>Twitch Link </td>
    <td>
      - Downloads VODs<br>
      - Downloads chat<br>
      - Able to render chat<br>
    </td>
    <td>
      - Doesn't download broadcasts<br>
      - Not automatic<br>
    </td>
  </tr>
</table>