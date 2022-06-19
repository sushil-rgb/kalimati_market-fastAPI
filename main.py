from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import random
import os

   
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"}

interval = 1

# opt = Options()
opt = webdriver.ChromeOptions()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# path = Service("c:\\users\\chromedriver.exe")

arguments = ['--no-sandbox', '--headless', 'start-maximized', "disable-infobars", "--disable-extensions","--disable-gpu",
             '--disable-dev-shm-usage', headers]


for arg in arguments:
    opt.add_argument(opt.add_experimental_option("detach", True))

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=opt)
# driver = webdriver.Chrome(service=path, options=opt)

base_url = "https://kalimatimarket.gov.np/"

 
def check_response(urls):
    return requests.get(urls)
 
 
def automation_kmarket():
    driver.maximize_window()
    driver.get(base_url)       
    # automation:
    driver.find_element(By.XPATH, '//*[@id="demo-swicher"]/header/div[3]/div/div/nav/ul/li[6]/a').click()  # clicks "Click Np Nepali tab""
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="demo-swicher"]/header/div[3]/div/div/nav/ul/li[6]/ul/li/a').click()  # clicks "GB English"
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="app"]/main/section[1]/div/div[1]/div/div[3]/div/div/div/div/div/div/a[1]').click()  # clicks check prices tab
        

def kalimati_market_en():   

    commodity_lists = []
    unit_lists = []
    minimum_lists = []
    maximum_lists = []
    average_lists = []  

    automation_kmarket()   
    
    for next in range(10):

        commodity_table = driver.find_element(By.ID, 'commodityDailyPrice').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
            
        for commodities in commodity_table:
            datas = commodities.find_elements(By.TAG_NAME, 'td')
            commodity_lists.append(datas[0].text.strip())
            unit_lists.append(datas[1].text.strip())
            minimum_lists.append(datas[2].text.strip())
            maximum_lists.append(datas[3].text.strip())
            average_lists.append(datas[4].text.strip())
            
        driver.find_element(By.ID, 'commodityDailyPrice_next').click()
        sleep(interval)
    
    return commodity_lists, unit_lists, minimum_lists, maximum_lists, average_lists
    


def date_header_en():   
    commodity_table = driver.find_element(By.ID, 'commodityDailyPrice').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    date_today = ""
    date = driver.find_elements(By.ID, 'commodityPricesDailyTable')

    for dat in date:
        date_today += dat.find_element(By.TAG_NAME, 'h5').text.strip()

    return date_today    
  


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

