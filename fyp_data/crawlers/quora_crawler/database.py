import pymongo
import pymongo.database
from model import Url
from model import Content

def insert_url_table(url: Url):
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    
    collection_name = "url"
    
    my_db.create_collection(collection_name) if my_db.get_collection(collection_name) is None else None
    
    url_collection: pymongo.database.Collection = my_db[collection_name]
    try:
        existing_url = url.find_one({"url": url.url})
        
        if existing_url:
            print(f"URL already exists: {existing_url}")
        else:
            print("Going to insert")
            result = url_collection.insert_one(vars(url))
            print(f"Inserted document with ID: {result.inserted_id}")

    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def insert_content_table(content: dict):
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    collection_name = "content"
    
    my_db.create_collection(collection_name) if my_db.get_collection(collection_name) is None else None
    
    content_collection: pymongo.database.Collection = my_db[collection_name]
    try:
        result = content_collection.insert_one(content)
        print(f"Inserted document with ID: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        my_client.close()
        
        
def update_content_table(content: dict):
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    content: pymongo.database.Collection = my_db["content"]
    try:
        filter_criteria = {"_id": content["_id"]}
        update_operation = {"$set": content}
        
        print("Going to update")
        result = content.update_one(filter_criteria, update_operation)
        
        if result.matched_count > 0:
            print(f"Updated document with ID: {content['_id']}")
        else:
            print("No matching document found for update.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
def get_all_url():
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    url: pymongo.database.Collection = my_db["url"]
    try:
        result = url.find()
        return list(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def get_all_content():
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    content: pymongo.database.Collection = my_db["content"]
    try:
        result = content.find()
        return list(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []