import json
from pydantic import BaseModel
from preprocessing.cleaning_data import preprocess
from typing import Literal
from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from predict.prediction import prediction



class Item(BaseModel):
    area: int
    property_type: Literal['APARTMENT', 'HOUSE', 'OTHERS']
    rooms_number: int
    zip_code: int
    land_area: int | None 
    garden: int | None 
    garden_area: int | None 
    equipped_kitchen: bool | None 
    full_address: str | None 
    swimming_pool: bool  | None 
    furnished: bool | None 
    open_fire: bool | None 
    terrace: bool | None 
    terrace_area: int | None 
    facades_number: int | None 
    building_state: Literal["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"] 


#PORT = os.environ.get("PORT", 8000)
my_awesome_api = FastAPI()

@my_awesome_api.get("/")
async def root():
    return {"alive"}


@my_awesome_api.post("/predict")
async def make_prediction(input: Item = Body(embed=True)):
    json_input = jsonable_encoder(input)
    processed_input = preprocess(json_input)
    #return processed_input
    predicted_value = prediction(processed_input)

    
    return predicted_value