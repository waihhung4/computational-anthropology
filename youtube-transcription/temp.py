import requests
import json

url = "https://youtube-v2.p.rapidapi.com/search/"

querystring = {"query":"sumerian","lang":"en"}

headers = {
	"x-rapidapi-key": "eb629002b7msh087fa9ab159db6ep10a1e2jsn5d5fb83ce4db",
	"x-rapidapi-host": "youtube-v2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

with open('sumerian.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)  # `indent` for pretty printing
