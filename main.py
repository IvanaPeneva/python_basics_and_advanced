import math

from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse

app = FastAPI()

#i used this calculator as a guidance https://www.omnicalculator.com/other/3d-printing
#the diameter of the fillament is the nozzle diameter
#elngth of the filament used for printing,
#time must be in minutes
#http://127.0.0.1:8000/api/calculator/?density=1&diameter=1&length=1&price=1&time=5&hourly_rate=13


@app.get("/api/calculator/")
async def calculator(density: float, diameter: float, length: float, price: float, time:int, hourly_rate:float):

    sum_price_printer= density * math.pi * pow((diameter / 2), 2) * length * price
    labour = time * hourly_rate
    endprice=sum_price_printer+labour #would be must better if rounded to the bigger with math.ceil

    #i would also add utilities( used electricity)
    return JSONResponse(
            content={
                'ENDPRICE':endprice,

                'calculatedPricePrinter': sum_price_printer,
                'density': density,
                'diameter': diameter,
                'length': length,
                'price for unit of the material': price,

                'labourCosts':labour,
                'time': time,
                'hourly_rate': hourly_rate

            },
            status_code=200)

'''
filament type	full name	density (g/cm³)
ABS	Acrylonitrile Butadiene Styrene	1.05
PLA	Polylactic Acid	1.27
PETG	Polyethylene Terephthalate	1.25
PETT	T-Glase filament	1.45
HIPS	High Impact Polystyrene	1.04
TPU	Thermoplastic Polyurethane	1.30
'''