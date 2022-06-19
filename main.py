from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from kalimati_market.functionsalities_sel import kalimati_market_en, date_header_en


app = FastAPI()
data_kMarket_en = kalimati_market_en()


@app.get("/kalimati_market")
def main_page():    
        return {'api-endpoints': [                            
                            "/kalimati_market",                            
                            "/kalimati_market/commodity",
                            "/kalimati_market/unit",
                            "/kalimati_market/minimum",
                            "/kalimati_market/maximum",
                            "/kalimati_market/average",
        ]}

         


@app.get("/kalimati_market/")
def market_today(): 

            return {date_header_en(): {
                "Commodity": data_kMarket_en[0],
                "Unit": data_kMarket_en[1],
                "Minimum": data_kMarket_en[2],
                "Maximum": data_kMarket_en[3],
                "Average": data_kMarket_en[4]
            }
            }

           
               
    

@app.get("/kalimati_market/commodity")
def commodity():         
        return {date_header_en():{
            "वस्तु":data_kMarket_en(0)}}
    

@app.get("/kalimati_market/unit")
def unit():
    return {date_header_en():{
            "वस्तु": data_kMarket_en(1)}}


@app.get("/kalimati_market/minimum")
def minimum():   
        return {date_header_en():{
            "वस्तु": data_kMarket_en(2)}}


@app.get("/kalimati_market/maximum")
def maximum():
   
        return {date_header_en():{
            "वस्तु": data_kMarket_en(3)}}


@app.get("/kalimati_market/average")
def average():   
         
        return {date_header_en():{
            "वस्तु": data_kMarket_en(4)}}

