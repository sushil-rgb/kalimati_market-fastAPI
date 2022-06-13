from dataclasses import dataclass
from fastapi import FastAPI
from kalimati_market.functionalities_bs4 import kalimati_market_np, date_header_np
from kalimati_market.functionalities_selenium import kalimati_market_en, date_header_en


app = FastAPI()
data_kMarket_en = kalimati_market_en()


def check_lang(langs, value1, value2):
    # langs = ""
    if langs == 'en':
        return value1
    elif langs == 'np':
        return value2
    else:
        return {"Details": "Not found",
                "Try:": "localhost/kalimati_market_en | localhost/kalimati_market/np"}


@app.get("/kalimati_market")
def main_page():
    return {'api-endpoints': [
                        "localhost/kalimati_market/np",
                        "localhost/kalimati_market/en",
                        "localhost/kalimati_market/np/commodity",
                        "localhost/kalimati_market/np/unit",
                        "localhost/kalimati_market/np/minimum",
                        "localhost/kalimati_market/np/maximum",
                        "localhost/kalimati_market/np/average",
                        "localhost/kalimati_market/en/commodity",
                        "localhost/kalimati_market/en/unit",
                        "localhost/kalimati_market/en/minimum",
                        "localhost/kalimati_market/en/maximum",
                        "localhost/kalimati_market/en/average"
    ]
           }        


@app.get("localhost/kalimati_market/{lang}")
def market_now(lang: str):
    return check_lang(lang,
       
            {date_header_en(): {
                "Commodity": data_kMarket_en[0],
                "Unit": data_kMarket_en[1],
                "Minimum": data_kMarket_en[2],
                "Maximum": data_kMarket_en[3],
                "Average": data_kMarket_en[4]
            }
            },

            {date_header_np(): {
                        "वस्तु": kalimati_market_np(0),
                        "एकाइ": kalimati_market_np(1),
                        "न्यूनतम": kalimati_market_np(2),
                        "अधिकतम": kalimati_market_np(3),
                        "औसत": kalimati_market_np(4)
                }
                }
            )    
    

@app.get("localhost/kalimati_market/{lang}/commodity")
def commodity(lang: str):
    return check_lang(lang, {
        date_header_en(): {
            "Commodity": data_kMarket_en[0]}}, 
        {date_header_np():{
            "वस्तु": kalimati_market_np(0)}})
    

@app.get("localhost/kalimati_market/{lang}/unit")
def unit(lang: str):
    return check_lang(lang, {
        date_header_en(): {
            "Commodity": data_kMarket_en[1]}}, 
        {date_header_np():{
            "वस्तु": kalimati_market_np(1)}})


@app.get("localhost/kalimati_market/{lang}/minimum")
def minimum(lang: str):
    return check_lang(lang, {
        date_header_en(): {
            "Commodity": data_kMarket_en[2]}}, 
        {date_header_np():{
            "वस्तु": kalimati_market_np(2)}})


@app.get("localhost/kalimati_market/{lang}/maximum")
def maximum(lang: str):
    return check_lang(lang, {
        date_header_en(): {
            "Commodity": data_kMarket_en[3]}}, 
        {date_header_np():{
            "वस्तु": kalimati_market_np(3)}})


@app.get("localhost/kalimati_market/{lang}/average")
def average(lang: str):
    return check_lang(lang, {
        date_header_en(): {
            "Commodity": data_kMarket_en[4]}}, 
        {date_header_np():{
            "वस्तु": kalimati_market_np(4)}})

