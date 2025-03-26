from typing import Optional
from db import *
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any frontend (use specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)



@app.get("/get_content")
def get_content(page: int = Query(1, alias="page", ge=1), limit: int = Query(10, alias="limit", ge=1), sortBy: str = Query(None, alias="sortBy"), order: str = Query(None, alias="order")):
    data = get_all_content(page=page, limit=limit, sortBy=sortBy, order=order)
    
    return {
        "page": page,
        "total_pages": 1174,
        "data": data
    }
    
    
@app.get("/get_url")
def get_url(page: int = Query(1, alias="page", ge=1), limit: int = Query(10, alias="limit", ge=1), sortBy: str = Query(None, alias="sortBy"), order: str = Query(None, alias="order")):
    data = get_all_url(page=page, limit=limit, sortBy=sortBy, order=order)
    
    return {
        "page": page,
        "total_pages": 42,
        "data": data
    }
    
    
@app.get("/get_image_mapping")
def get_url(page: int = Query(1, alias="page", ge=1), limit: int = Query(10, alias="limit", ge=1), sortBy: str = Query(None, alias="sortBy"), order: str = Query(None, alias="order")):
    data = get_image_mapping(page=page, limit=limit, sortBy=sortBy, order=order)
    
    return data