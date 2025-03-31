import pymongo
import pymongo.database

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