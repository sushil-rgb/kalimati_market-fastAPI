from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# from main import data
import time

'''def kalimati_market(value):
    commodity_table = driver.find_element(By.ID, 'commodityDailyPrice').find_elements(By.TAG_NAME, 'td')

    if value == 1:
        products = []
        for a in commodity_table[::5]:
            products.append(a.text)
        return products

    if value == 2:
        units = []
        for b in commodity_table[1::5]:
            units.append(b.text)
        return units

    if value == 3:
        minimum = []
        for c in commodity_table[2::5]:
            minimum.append(c.text)
        return minimum

    if value == 4:
        maximum = []
        for d in commodity_table[3::5]:
            maximum.append(d.text)
        return maximum

    if value == 5:
        average = []
        for e in commodity_table[4::5]:
            average.append(e.text)
        return average'''

# first approach
'''commodity_table = driver.find_element(By.ID, 'commodityDailyPrice').find_elements(By.TAG_NAME, 'td')

        for a in commodity_table[row1::row2]:
            products.append(a.text)
        if row == 6:
            driver.execute_script('scrollBy(0, -500);')
            for i in range(1, 14):
                if i % 2 == 0:
                    continue
                time.sleep(1)
                plus_sign = driver.find_element(By.XPATH, f'//*[@id="commodityDailyPrice"]/tbody/tr[{i}]/td[1]').click()
            for r in range(2, 15):
                if r % 2 != 0:
                    continue
                average = driver.find_element(By.XPATH,
                                              f'//*[@id="commodityDailyPrice"]/tbody/tr[{r}]/td/ul/li/span[2]')
                products.append(average.text)
                time.sleep(1)'''

