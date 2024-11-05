import pymongo
import pymongo.database
from model import Url
from model import Content

def insert_url_table(url: Url):
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    crawlers_url: pymongo.database.Collection = my_db["crawlers_url"]
    try:
        existing_url = crawlers_url.find_one({"url": url.url})
        
        if existing_url:
            print(f"URL already exists: {existing_url}")
        else:
            print("Going to insert")
            result = crawlers_url.insert_one(vars(url))
            print(f"Inserted document with ID: {result.inserted_id}")

    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def insert_content_table(content: Content):
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    crawlers_content: pymongo.database.Collection = my_db["crawlers_content"]
    try:
        
        print("Going to insert")
        result = crawlers_content.insert_one(vars(content))
        print(f"Inserted document with ID: {result.inserted_id}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
def get_all_url():
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    crawlers_url: pymongo.database.Collection = my_db["crawlers_url"]
    try:
        result = crawlers_url.find()
        return list(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def get_all_content():
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    crawlers_content: pymongo.database.Collection = my_db["crawlers_content"]
    try:
        result = crawlers_content.find()
        return list(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []