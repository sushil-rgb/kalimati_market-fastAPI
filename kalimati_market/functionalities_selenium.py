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
import itertools
import pandas as pd
import concurrent.futures
import random
import winsound
 
def get_ua():
    uastrings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 "
        "Safari/600.1.25",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 "
        "Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 "
        "Safari/537.85.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
    ]
 
    return random.choice(uastrings)
headers = {'User-Agent': get_ua()}
interval = 1
headless = True
path = Service('c:\\users\\chromedriver.exe')
opt = Options()
arguments = ['--headless',  f'user-agent= {get_ua()}',
             'disable-notifications', "--window-size=1920,1080", "--start-maximized"]


 
if headless:
    for arg in arguments:
        opt.add_argument(arg)
else:
    for arg in arguments[1:]:
        opt.add_argument(arg)
 
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=path, options=opt)


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
  

