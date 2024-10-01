import pymongo
import pymongo.database
from model import Url

my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db: pymongo.database.Database = my_client["final-year-project"]

CRAWLERS_URL: pymongo.database.Collection = my_db["crawlers_url"]
CRAWLERS_CONTENT: pymongo.database.Collection = my_db["crawlers_content"]

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
        
def get_all_url():
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    crawlers_url: pymongo.database.Collection = my_db["crawlers_url"]
    try:
        result = crawlers_url.find()
        return list(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
url_table_list = get_all_url()
        