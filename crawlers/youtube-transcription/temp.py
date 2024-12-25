import requests
import json


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
print(get_video_id_list("sumerian"))