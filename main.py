from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

dir=os.path.dirname(__file__)
json_folder = "2079-json"

app=FastAPI()

@app.get('/',response_class=JSONResponse)
async def root():
    return JSONResponse({"message":"Hello World"})

@app.get('/data/baisakh',response_class=JSONResponse)
async def data():
    file=open("2079-json/baisakh-2079.json")
    return JSONResponse(json.load(file))


@app.get("/{data}", response_class=JSONResponse)
async def get_data(data):
    json_file = os.path.join(dir, json_folder, f"{data}.json")
    
    if os.path.exists(json_file):
        with open(json_file) as file:
            data = json.load(file)
        return JSONResponse(data)
    
    return JSONResponse({"ERROR": "File not found"})
