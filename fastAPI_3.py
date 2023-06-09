from fastapi import FastAPI
from math import sqrt

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/distance/{lat1}/{lat2}/{lon1}/{lon2}")
async def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    # Calculate the distance between two points using the distance formula
    distance = sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    return {"distance": distance}

# sample input   -->       http://127.0.0.1:8000/distance/1/2/3/4    Result --> {"distance":1.4142135623730951}