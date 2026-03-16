from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.models.planet import Planet
from src.controllers.planet import PlanetController

app = FastAPI()

class PlanetRequest(BaseModel):
    name: str
    mass: float
    radius: float

@app.get("/planets")
async def get_planets():
    return PlanetController.get_all_planets()

@app.post("/planets")
async def create_planet(request: PlanetRequest):
    return PlanetController.create_planet(request)
