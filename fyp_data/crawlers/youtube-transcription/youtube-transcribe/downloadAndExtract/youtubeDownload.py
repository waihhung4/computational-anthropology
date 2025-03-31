import yt_dlp
import os

def download_youtube_audio(url, output_path):
    # Configure yt-dlp options
    if os.path.exists(output_path):
        print(f"File already exists: {output_path}")
        return
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': output_path,
    }

    # Download the audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])