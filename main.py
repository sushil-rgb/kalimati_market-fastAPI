from dataclasses import dataclass
from fastapi import FastAPI
from kalimati_market.functionalities_bs4 import kalimati_market_np, date_header_np
from kalimati_market.functionalities_selenium import kalimati_market_en, date_header_en


app = FastAPI()
data_kMarket_en = kalimati_market_en()



@app.get("/kalimati_market/np")
def market_now_np():                
    return {date_header_np(): {
                    "वस्तु": kalimati_market_np(0),
                    "एकाइ": kalimati_market_np(1),
                    "न्यूनतम": kalimati_market_np(2),
                    "अधिकतम": kalimati_market_np(3),
                    "औसत": kalimati_market_np(4)
            }}


@app.get("/kalimati_market/en")
def market_now_en(): 
    return {date_header_en(): {
            "Commodity": data_kMarket_en[0],
            "Unit": data_kMarket_en[1],
            "Minimum": data_kMarket_en[2],
            "Maximum": data_kMarket_en[3],
            "Average": data_kMarket_en[4]

        } }
            

@app.get("/kalimati_market/en/commodity")
def commodity():
    return {date_header_en(): {"Commodity": data_kMarket_en[0]}}


@app.get("/kalimati_market/en/unit")
def unit():
    return {date_header_en(): {"Unit": data_kMarket_en[1]}}


@app.get("/kalimati_market/en/minimum")
def minimum():
    return {date_header_en(): {"Minimum": data_kMarket_en[2]}}


@app.get("/kalimati_market/en/maximum")
def maximum():
    return {date_header_en(): {"Maximum": data_kMarket_en[3]}}


@app.get("/kalimati_market/en/average")
def average():
    return {date_header_en(): {"Average": data_kMarket_en[4]}}


# Nepali
@app.get("/kalimati_market/np/commodity")
def commodity():
    return {date_header_np(): {"वस्तु": kalimati_market_np(0)}}


@app.get("/kalimati_market/np/unit")
def unit():
    return {date_header_np(): {"एकाइ": kalimati_market_np(1)}}


@app.get("/kalimati_market/np/minimum")
def minimum():
    return {date_header_np(): {"न्यूनतम": kalimati_market_np(2)}}


@app.get("/kalimati_market/np/maximum")
def maximum():
    return {date_header_np(): {"अधिकतम": kalimati_market_np(3)}}

@app.get("/kalimati_market/np/average")
def average():
    return {date_header_np(): {"औसत": kalimati_market_np(4)}}
