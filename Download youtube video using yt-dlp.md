## 1. Download yt-dlp (to download audio and video file )
Ensure you have latest python and pip package manager in it.
Then open powershell and give following command-
```
pip install yt-dlp
```
## Download ffmpeg (to merge the downloaded video and audio)
### 1. Search for file
```
winget search ffmpeg
```
### Download ffmpeg (should come on top, mine was Gyan.FFmpeg)
```
winget install Gyan.FFmpeg
```
## Happy downloading in super speed (1080p)-
```
yt-dlp -f 'bestvideo[height=1080]+bestaudio/best[height=1080]' "Youtube video/playlist link (within inverted comma)"
```


## For music/ audio only
```
yt-dlp -f bestaudio --extract-audio --audio-format mp3 "https://youtu.be/sVkSjrUaatg?si=od7hc5-87CuvnWho"
```
This will download the audio and convert it to MP3 format automatically.
Convert to MP3 using ffmpeg (if needed):
If you download the video using a different format, use ffmpeg to convert it:
```
ffmpeg -i input_video.mp4 output.mp3
```


## Enjoy!
