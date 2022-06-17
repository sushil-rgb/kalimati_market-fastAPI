from time import sleep
from bs4 import BeautifulSoup
import requests
import random


# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"}

url = "https://kalimatimarket.gov.np/#commodityPricesDailyTable"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


def date_header_np():    
    table = soup.find('table', id='commodityDailyPrice').find('tbody').find_all('tr')    
    date = soup.find_all('div', id='commodityPricesDailyTable')
     
    for dat in date:
        return dat.find('h5').text


table = soup.find('table', id='commodityDailyPrice').find('tbody').find_all('tr')


def kalimati_market_np(value):
    # This technique is list comprehension:
    # It stores pulled data and store in lists: Less code and runs fast: It's quite powerful in Python
    lists = [(tab.find_all('td'))[value].text for tab in table]
    return lists


'''def kalimati_market(value):
    lists = []  # creating empty lists to store values after scraping the needed datas:
    for tab in table:  # looping through table and grabbing data from their respective columns
        datas = tab.find_all('td')  # this html tag has the date we need to pull and save in Excel sheet:
        lists.append(datas[value].text) '''

