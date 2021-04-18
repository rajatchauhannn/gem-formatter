#https://bidplus.gem.gov.in/advance-search?state_name=DELHI&city_name=CENTRAL+DELHI&from_date=18-04-2021&to_date=30-04-2021&searchlocation=Search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

url = "https://bidplus.gem.gov.in/advance-search?state_name=DELHI&city_name=CENTRAL+DELHI&from_date=18-04-2021&to_date=30-04-2021&searchlocation=Search"
dirname = os.getcwd()
path = os.path.join(dirname, "media/geckodriver")

driver = webdriver.Firefox(executable_path=path)
driver.get(url)

WebDriverWait(driver, 10)

items = driver.find_elements_by_xpath("//span[contains(text(), 'All in One PC') or contains(text(), 'Desktop Computers')]")

for element in items:
    # print(element.text)
    element = element.find_element_by_xpath("..")
    element = element.find_element_by_xpath("..")
    parent = element.find_element_by_xpath("..")

    print(parent.text[8:26])
    bid_type = parent.text[8:11]
    bid_year = parent.text[12:16]
    bid_let = parent.text[17:18]
    bid_dig = parent.text[19:26]
    #https://bidplus.gem.gov.in/advance-search?bno=GEM%2F2021%2FB%2F1161309&category=&searchbid=Search
    #https://bidplus.gem.gov.in/advance-search?bno={bid_type}%2F{bid_year}%2F{bid_let}%2F{bid_dig}&category=&searchbid=Search

    req = Request(f"https://bidplus.gem.gov.in/advance-search?bno={bid_type}%2F{bid_year}%2F{bid_let}%2F{bid_dig}&category=&searchbid=Search")
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    for link in links:
        if link[:5] =='/show' :
            print(link)
