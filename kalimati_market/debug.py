from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

opt = Options()
path = Service('c:\\users\\chromedriver.exe')

url = "https://kalimatimarket.gov.np/#commodityPricesDailyTable"
driver = webdriver.Chrome(service=path, options=opt)

args = ["""user-agent= Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) 
    NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US""", """--headless"""]
for arg in args:
    opt.add_argument(arg)


# driver.set_window_position(-10000, 0)
driver.maximize_window()
driver.get(url)

date = driver.find_element(By.CSS_SELECTOR, '#commodityPricesDailyTable > div > div > div > h5').text
time.sleep(1)


def kalimati_market(value):

    products = []
    while True:
        count = 1
        for i in range(1, 11):
            lists = driver.find_element(By.XPATH, f'//*[@id="commodityDailyPrice"]/tbody/tr[{i}]/td[{value}]').text
            products.append(lists)
        next_page = driver.find_element(By.XPATH, '//*[@id="commodityDailyPrice_next"]').click()
        count += 1
        time.sleep(1)
        if count == 10:
            break

    return products


'''//*[@id="commodityDailyPrice"]/tbody/tr[1]/td[1]
//*[@id="commodityDailyPrice"]/tbody/tr[10]/td[1]
//*[@id="commodityDailyPrice"]/tbody/tr[1]/td[2]
'''
# Initializing values:
products_lists = kalimati_market(1)
units = kalimati_market(1)
minimum = kalimati_market(2)
maximum = kalimati_market(3)
averages = kalimati_market(4)
# averages = [i for i in kalimati_market(6) if i not in ['के.जी.', 'के जी', 'केजी', 'दर्जन', 'के.जी', 'प्रति गोटा']]
driver.close()


print(products_lists)
print(units)
print(minimum)
print(maximum)


# Pandas dataframes:
