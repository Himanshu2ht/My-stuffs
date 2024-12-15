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
## Enjoy!
