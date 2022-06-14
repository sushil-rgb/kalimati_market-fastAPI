import json
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import StaleElementReferenceException
from functionalities_bs4 import get_ua
import itertools
import pandas as pd
import concurrent.futures
import random
import os

   
headers = {'User-Agent': get_ua()}
interval = 1
headless = True

opt = Options()
opt = webdriver.ChromeOptions()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# path = Service("c:\\users\\chromedriver.exe")
arguments = ['--headless',  f'user-agent= {get_ua()}',
             'disable-notifications', "--window-size=1920,1080", "--start-maximized", 
             '--disable-dev-shm-usage', '--no-sandbox']


 
if headless:
    for arg in arguments:
        opt.add_argument(arg)
else:
    for arg in arguments[1:]:
        opt.add_argument(arg)
 
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=opt)
# driver = webdriver.Chrome(service=path, options=opt)

base_url = "https://kalimatimarket.gov.np/"

 
def check_response(urls):
    return requests.get(urls)
 
 
# convert multi-dimensional list to single dimensional one:
def flattened_list(lists):
    flat = list(itertools.chain(*lists))
    return flat
 
 
# using concurrency (multithreading) features for faster scraping:
def lightning_scraping(functions, lists):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executions = executor.map(functions, lists)
        return executions


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
  

