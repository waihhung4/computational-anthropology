import pymongo
import base64
from fastapi.responses import JSONResponse
from bson import Binary
import pandas as pd
import numpy as np

def get_all_url(page: int = 1, limit: int = 10, sortBy: int = None, order: int = None):
    with pymongo.MongoClient("mongodb://localhost:27017/") as my_client:
        my_db = my_client["final-year-project"]
        url_collection = my_db["url"]
        
        try:
            skip = (page - 1) * limit
            order = pymongo.ASCENDING if order == "asc" else pymongo.DESCENDING
            if sortBy is None:
                result = list(url_collection.find().skip(skip).limit(limit))
            else:
                result = list(url_collection.find().skip(skip).limit(limit).sort(sortBy, order))
            for item in result:
                item["_id"] = str(item["_id"])
        except Exception as e:
            print(f"An error occurred: {e}")
            return []   
    return result

def get_all_content(page: int = 1, limit: int = 10, sortBy: str = None, order: str = None):
    with pymongo.MongoClient("mongodb://localhost:27017/") as my_client:
        my_db = my_client["final-year-project"]
        content_collection = my_db["final_content"]
        try:
            skip = (page - 1) * limit
            order_val = pymongo.ASCENDING if order == "asc" else pymongo.DESCENDING
            
            if sortBy is None:
                result = list(content_collection.find().skip(skip).limit(limit))
            else:
                result = list(content_collection.find().skip(skip).limit(limit).sort(sortBy, order_val))
            
            # Debugging: Check for NaN or Inf values
            for item in result:
                for key, value in item.items():
                    if isinstance(value, float):
                        if np.isnan(value) or np.isinf(value):
                            print(f"Found invalid float in item {item['_id']}, key: {key}, value: {value}")
                item["_id"] = str(item["_id"])
                item["topics"] = str(item["topics"])
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    return result

def get_image_mapping(page: int = 1, limit: int = 10, sortBy: int = None, order: int = None):
    output = {}
    with pymongo.MongoClient("mongodb://localhost:27017/") as my_client:
        my_db = my_client["final-year-project"]
        image_mapping_collection = my_db["image_mapping"]

        skip = (page - 1) * limit
        order = pymongo.ASCENDING if order == "asc" else pymongo.DESCENDING
        df = pd.DataFrame(image_mapping_collection.find())
        df.drop(columns=['resnet_chinese_image_features', 'resnet_sumerian_image_features', 'dino_v2_chinese_image_features', 'dino_v2_sumerian_image_features'], inplace=True)
        resnet152_threshold = df['resnet_similarity_score'].mean() + df['resnet_similarity_score'].std()
        dinov2_threshold = df['dinov2_similarity_score'].mean() + df['dinov2_similarity_score'].std()
        ssim_threshold = df['ssim_similarity_score'].mean() + df['ssim_similarity_score'].std()
        total_pages = df.shape[0] // limit + 1
        if sortBy is None:
            result = list(image_mapping_collection.find().skip(skip).limit(limit))
        else:
            result = list(image_mapping_collection.find().skip(skip).limit(limit).sort(sortBy, order))

        for i in range(len(result)):
            result[i]["_id"] = str(result[i]["_id"])
            result[i]["chinese_image"] = base64.b64encode(result[i]["chinese_image"]).decode("utf-8")
            result[i]["sumerian_image"] = base64.b64encode(result[i]["sumerian_image"]).decode("utf-8")
            result[i]["resnet_chinese_image_features"] = base64.b64encode(result[i]["resnet_chinese_image_features"]).decode("utf-8")
            result[i]["resnet_sumerian_image_features"] = base64.b64encode(result[i]["resnet_sumerian_image_features"]).decode("utf-8")
            result[i]["dino_v2_chinese_image_features"] = base64.b64encode(result[i]["dino_v2_chinese_image_features"]).decode("utf-8")
            result[i]["dino_v2_sumerian_image_features"] = base64.b64encode(result[i]["dino_v2_sumerian_image_features"]).decode("utf-8")
            
        output["total_pages"]  = int(total_pages)
        output["page"]  = page
        output["data"] = result
        output["resnet152_threshold"] = resnet152_threshold
        output["dinov2_threshold"] = dinov2_threshold
        output["ssim_threshold"] = ssim_threshold
        return output
