from youtube_transcript_api import YouTubeTranscriptApi
from downloadAndExtract.youtubeDownload import download_youtube_audio
from downloadAndExtract.transcribe import transcribe
import json
import multiprocessing
import os
import requests
from database import insert_content_table

FILENAME = "youtube-transcribe/source.txt"
MAX_PROCESSES = 4

search_keyword_list = ["Sumerian anthropology", "ancient anthropology", "shang dynasty", "sumerian civilization", "xia dynasty", "sumerian history", "sumerian chinese"]


def get_video_id_list(search_keyword):
    
    result = []
    url = "https://youtube-v2.p.rapidapi.com/search/"

    querystring = {"query":f"{search_keyword}","lang":"en"}

    headers = {
        "x-rapidapi-key": "eb629002b7msh087fa9ab159db6ep10a1e2jsn5d5fb83ce4db",
        "x-rapidapi-host": "youtube-v2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code != 200:
        print(f"Error fetching video list for {search_keyword}")
        return result
    
    for video in response.json().get('videos'):
        if video["type"] == "NORMAL":
            result.append(video["video_id"]) 
    continuation_token = response.json().get('continuation_token')
    
    continuation_url = "https://youtube-v2.p.rapidapi.com/search/continuation"
    
    for i in range(2):
        querystring = {"continuation_token":f"{continuation_token}","query":f"{search_keyword}","lang":"en"}
        response = requests.get(continuation_url, headers=headers, params=querystring)
        if response.status_code != 200:
            print(f"Error fetching video list for {search_keyword}")
            return result
        
        for video in response.json().get('videos'):
            if video["type"] == "NORMAL":
                result.append(video["video_id"]) 
        
        continuation_token = response.json().get('continuation_token')
        
    return result
    
    
    
def save_transcript(file_name, result):
    os.makedirs('outputs', exist_ok=True)
    with open(f'outputs/{file_name}.json', "w") as file:
        json.dump(result, file, indent=4)

def transcript_exists(video_id):
    return os.path.exists(f'outputs/{video_id}.json')

def process_video(video_id, search_keyword):
    video_id = video_id.strip()
    
    url = f"https://www.youtube.com/watch?v={video_id}"
    source = "youtube"
    
    if transcript_exists(video_id):
        print(f"Transcript already exists for video: {video_id}. Skipping.")
        return
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(language_codes=['en'])
        subtitle = transcript.fetch()
        
        result = ""
        
        for sub in subtitle:
            result += sub['text'] + " "
        save_transcript(video_id, result)
        insert_content_table({"text": result, "search_keyword": search_keyword, "url": url, "source": source})
        print(f"Processed transcript for video: {video_id}")
    except Exception as e:
        print(f"Error processing transcript for {video_id}. Downloading audio...")
        try:
            os.makedirs('audios', exist_ok=True)
            download_youtube_audio(f"https://www.youtube.com/watch?v={video_id}", f"audios/{video_id}")
            result = transcribe(f"audios/{video_id}.mp3")["text"]
            save_transcript(video_id, result)
            insert_content_table({"text": result, "search_keyword": search_keyword, "url": url, "source": source})
            print(f"Processed audio for video: {video_id}")
        except Exception as e:
            print(f"Error processing audio for {video_id}: {str(e)}")

if __name__ == "__main__":
    for search_keyword in search_keyword_list:
        video_id_list = get_video_id_list(search_keyword)
        # with multiprocessing.Pool(processes=MAX_PROCESSES) as pool:
        #     pool.map(process_video, video_id_list)
        
        for video_id in video_id_list:
            process_video(video_id, search_keyword)