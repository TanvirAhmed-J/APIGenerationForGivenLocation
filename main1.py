
from typing import Optional
from geopy.geocoders import Nominatim

from fastapi import FastAPI
import json
from pydantic import BaseModel
geolocator = Nominatim(user_agent="mytracer")

class Item(BaseModel):
   City : str
   Country: str

app = FastAPI()


@app.post("/items/")
async def create_item(item : Item) :
   loc = geolocator.geocode(item.City+','+item.Country)
   print(loc.latitude)
   print(loc.longitude)
   return { "Coordinates" :
      {"Longitude" : loc.longitude, "Latitude":loc.latitude},
      "City":item.City,
      "Country":item.Country
       }
