from dataclasses import dataclass
from fastapi import FastAPI
from kalimati_market.functionalities_bs4 import kalimati_market_np, date_header_np
from kalimati_market.functionalities_selenium import kalimati_market_en, date_header_en


app = FastAPI()
data_kMarket_en = kalimati_market_en()



@app.get("/kalimati_market/{lang}")
def market_now(lang: str): 
    if lang == 'np':               
        return {date_header_np(): {
                        "वस्तु": kalimati_market_np(0),
                        "एकाइ": kalimati_market_np(1),
                        "न्यूनतम": kalimati_market_np(2),
                        "अधिकतम": kalimati_market_np(3),
                        "औसत": kalimati_market_np(4)
                }}

    elif lang == 'en':
        return {date_header_en(): {
                "Commodity": data_kMarket_en[0],
                "Unit": data_kMarket_en[1],
                "Minimum": data_kMarket_en[2],
                "Maximum": data_kMarket_en[3],
                "Average": data_kMarket_en[4]

            }}
    
    else:
        return {"Details": "Not found"}
            

@app.get("/kalimati_market/{lang}/commodity")
def commodity(lang: str):
    if lang == 'en':
        return {date_header_en(): {"Commodity": data_kMarket_en[0]}}
    elif lang == 'np':
        return {date_header_np(): {"वस्तु": kalimati_market_np(0)}}
    else:
        return {"Details": "Not found"}


@app.get("/kalimati_market/{lang}/unit")
def unit(lang: str):
    if lang == 'en':
        return {date_header_en(): {"Unit": data_kMarket_en[1]}}
    elif lang == 'np':
        return {date_header_np(): {"एकाइ": kalimati_market_np(1)}}
    else:
        return {"Details": "Not found"}


@app.get("/kalimati_market/{lang}/minimum")
def minimum(lang: str):
    if lang == 'en':
        return {date_header_en(): {"Minimum": data_kMarket_en[2]}}
    elif lang == 'np':
        return {date_header_np(): {"्यूनतम": kalimati_market_np(2)}}
    else:
        return {"Details": "Not found"}


@app.get("/kalimati_market/{lang}/maximum")
def maximum(lang: str):
    if lang == 'en':
        return {date_header_en(): {"Maximum": data_kMarket_en[3]}}
    elif lang == 'np':
        return {date_header_np(): {"अधिकतम": kalimati_market_np(3)}}
    else:
        return {"Details": "Not found"}


@app.get("/kalimati_market/{lang}/average")
def average(lang: str):
    if lang == 'en':
        return {date_header_en(): {"Average": data_kMarket_en[4]}}
    elif lang == 'np':
        return {date_header_np(): {"औसत": kalimati_market_np(4)}}
    else:
        return {"Details": "Not found"}

