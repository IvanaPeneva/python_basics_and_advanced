from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse

app = FastAPI()

#http://127.0.0.1:8000/api/calculator/?neededMaterial=24593&price=0.007
#neededMaterial is from the Gcode smth like EXTRUDER_TRAIN.0.MATERIAL.VOLUME_USED:24593


@app.get("/api/calculator/")
async def calculator(neededMaterial: float, price: float):

    sumPrice=neededMaterial*price
    return JSONResponse(
            content={
                "calculatedPrice": sumPrice,
                'price for unit of the material': price,
                'needed material': neededMaterial,

            },
            status_code=200)