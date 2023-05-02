#! /mnt/sda/Documents/projects/graduate_work/backend/env/bin/python

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError
from tortoise import Tortoise
from src.models import Dish, Picture, User, Video
import uvicorn
import json

config: dict 
with open("config.json", "r") as c_file:
    config = json.load(c_file)


app = FastAPI()

register_tortoise(app=app, config=config["database"])


app.add_middleware(
   CORSMiddleware,
   allow_origins=config["cors"]["allowed_origins"],
   allow_credentials=True,
   allow_methods=config["cors"]["allowed_methods"],
   allow_headers=config["cors"]["allowed_headers"],
)


async def init_db():
    await Tortoise.init(config=config["database"])
    await Tortoise.generate_schemas()
    

@app.get("/")
async def root():
    return {"hello": "world"}

if __name__ == "__main__":
    uvicorn.run(app, host=config["server"]["host"], port=config["server"]["port"])

