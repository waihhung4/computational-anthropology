import pymongo
import pymongo.database

def insert_content_table(content: dict):
    my_client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db: pymongo.database.Database = my_client["final-year-project"]
    crawlers_content: pymongo.database.Collection = my_db["crawlers_content"]
    try:
        
        print("Going to insert")
        result = crawlers_content.insert_one(content)
        print(f"Inserted document with ID: {result.inserted_id}")
        
    except Exception as e:
        print(f"An error occurred: {e}")