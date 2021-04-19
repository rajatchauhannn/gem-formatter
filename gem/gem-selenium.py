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

dirname = os.getcwd()
path = os.path.join(dirname, "media/operadriver")
driver = webdriver.Opera(executable_path=path)
url = "https://bidplus.gem.gov.in/advance-search?state_name=DELHI&city_name=CENTRAL+DELHI&from_date=18-04-2021&to_date=30-04-2021&searchlocation=Search&page_no=1"
driver.get(url)
flag = driver.find_elements_by_xpath("//strong[contains(text(), 'Empty!')]")
pageno = 1
while (flag == []):
    url = f"https://bidplus.gem.gov.in/advance-search?state_name=DELHI&city_name=CENTRAL+DELHI&from_date=18-04-2021&to_date=30-04-2021&searchlocation=Search&page_no={pageno}"

    driver.get(url)

    items = driver.find_elements_by_xpath("//span[contains(text(), 'All in One PC') or contains(text(), 'Desktop Computers') or contains(text(), 'Server')]")

    for element in items:
        print(element.text)
        element = element.find_element_by_xpath("..")
        element = element.find_element_by_xpath("..")
        parent = element.find_element_by_xpath("..")

        link = parent.find_element_by_xpath("//a[contains(@href, '/show')]").click()
        WebDriverWait(driver, 1000)

    flag = driver.find_elements_by_xpath("//strong[contains(text(), 'Empty!')]")
    pageno+= 1

driver.quit()