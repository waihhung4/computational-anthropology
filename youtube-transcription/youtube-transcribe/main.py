from youtube_transcript_api import YouTubeTranscriptApi
from downloadAndExtract.youtubeDownload import download_youtube_audio
from downloadAndExtract.transcribe import transcribe
import json
import multiprocessing
import os

FILENAME = "youtube-transcribe/source.txt"
MAX_PROCESSES = 4

def save_transcript(file_name, result):
    os.makedirs('outputs', exist_ok=True)
    with open(f'outputs/{file_name}.json', "w") as file:
        json.dump(result, file, indent=4)

def transcript_exists(video_id):
    return os.path.exists(f'outputs/{video_id}.json')

def process_video(video_id):
    video_id = video_id.strip()
    
    if transcript_exists(video_id):
        print(f"Transcript already exists for video: {video_id}. Skipping.")
        return
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(language_codes=['en'])
        save_transcript(video_id, transcript.fetch())
        print(f"Processed transcript for video: {video_id}")
    except Exception as e:
        print(f"Error processing transcript for {video_id}. Downloading audio...")
        try:
            os.makedirs('audios', exist_ok=True)
            download_youtube_audio(f"https://www.youtube.com/watch?v={video_id}", f"audios/{video_id}")
            result = transcribe(f"audios/{video_id}.mp3")
            save_transcript(video_id, result)
            print(f"Processed audio for video: {video_id}")
        except Exception as e:
            print(f"Error processing audio for {video_id}: {str(e)}")

if __name__ == "__main__":
    with open(FILENAME, 'r') as file:
        video_id_list = file.readlines()

    with multiprocessing.Pool(processes=MAX_PROCESSES) as pool:
        pool.map(process_video, video_id_list)