from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.index.index import index_router

app = FastAPI()

# origins: List[str] = ["*"]
origins: List[str] = ["http://localhost:4200"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
    
prefix = "/bar/service/v1"

app.include_router(index_router, prefix=prefix, tags=["index"])
