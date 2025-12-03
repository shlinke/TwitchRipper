# TwitchRipper

TwitchRipper is a Python script that automatically downloads Twitch streams, archives VODs, and posts live notifications to Discord.

---

## Features
- Automatically detects when a Twitch channel goes live
- Downloads streams live using Streamlink
- Downloads VODs and chat using TwitchDownloaderCLI
- Merges broadcast and VOD audio with FFmpeg
- Sends notifications and updates to a Discord webhook
- Downloads VODs before they can be muted or deleted.

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
![](https://assets.shlinke.tech/code.png)
4. To run the script type "python TwitchRipper.py" in a terminal window.
![](https://assets.shlinke.tech/terminal.png)
---

## Why TwitchRipper?

TwitchRipper combines the best features of similar tools like StreamRecorder, TwitchDownloader, and TwitchLink.

>⚠️ Note: This script uses **a lot** of storage and works best on a computer running 24/7. <br>
>1 hour of a 1080p60fps stream ≈ 2.5GB.

**Example of archived streams** (~35 streams ≈ 385GB):
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