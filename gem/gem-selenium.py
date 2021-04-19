#https://bidplus.gem.gov.in/advance-search?state_name=DELHI&city_name=CENTRAL+DELHI&from_date=18-04-2021&to_date=30-04-2021&searchlocation=Search

from selenium import webdriver
import os
import datetime
from datetime import timedelta
from selenium.webdriver.opera.options import Options

dirname = os.getcwd()
OPERADRIVER_PATH = os.path.join(dirname, "media/operadriver")

driver = webdriver.Opera(executable_path=OPERADRIVER_PATH)

def find_and_download(state,city,start_date,end_date):
    flag = driver.find_elements_by_xpath("//strong[contains(text(), 'Empty!')]")
    url = f"https://bidplus.gem.gov.in/advance-search?state_name={state}&city_name={city}&from_date={start_date}&to_date={end_date}&searchlocation=Search&page_no=1"
    driver.get(url)
    pageno = 1
    while (flag == []):
        url = f"https://bidplus.gem.gov.in/advance-search?state_name={state}&city_name={city}&from_date={start_date}&to_date={end_date}&searchlocation=Search&page_no={pageno}"

        driver.get(url)

        items = driver.find_elements_by_xpath("//span[contains(text(), 'All in One PC') or contains(text(), 'Desktop Computers') or contains(text(), 'Server') or contains(text(), 'Laptop-Notebook') or contains(text(), 'Laptop')]")

        for element in items:
            print(element.text)
            element = element.find_element_by_xpath("..")
            element = element.find_element_by_xpath("..")
            parent = element.find_element_by_xpath("..")


            bid_let = parent.text[17:18]
            if bid_let == 'B':
                parent.find_element_by_xpath(f"//a[contains(text(), '{parent.text[8:26]}')]").click()

            elif bid_let == 'A':
                parent.find_element_by_xpath(f"//a[contains(text(), '{parent.text[7:24]}')]").click()


        flag = driver.find_elements_by_xpath("//strong[contains(text(), 'Empty!')]")
        pageno+= 1
    

current_date = datetime.datetime.strptime(str(datetime.datetime.now().date()), "%Y-%m-%d").strftime('%d-%m-%Y')

future_date = datetime.datetime.strptime(str(datetime.datetime.now().date() + timedelta(days=15)), "%Y-%m-%d").strftime('%d-%m-%Y')



#DELHI
find_and_download('DELHI','CENTRAL+DELHI',current_date,future_date)
find_and_download('DELHI','EAST+DELHI',current_date,future_date)
find_and_download('DELHI','NEW+DELHI',current_date,future_date)
find_and_download('DELHI','NORTH+DELHI',current_date,future_date)
find_and_download('DELHI','NORTH+EAST+DELHI',current_date,future_date)
find_and_download('DELHI','SHAHDARA',current_date,future_date)
find_and_download('DELHI','SOUTH+DELHI',current_date,future_date)
find_and_download('DELHI','SOUTH+EAST+DELHI',current_date,future_date)
find_and_download('DELHI','SOUTH+WEST+DELHI',current_date,future_date)
find_and_download('DELHI','WEST+DELHI',current_date,future_date)

#UP
find_and_download('UTTAR+PRADESH','AGRA',current_date,future_date)
find_and_download('UTTAR+PRADESH','ALIGARH',current_date,future_date)
find_and_download('UTTAR+PRADESH','ALLAHABAD',current_date,future_date)
find_and_download('UTTAR+PRADESH','AMBEDKAR+NAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','AURAIYA',current_date,future_date)
find_and_download('UTTAR+PRADESH','AZAMGARH',current_date,future_date)
find_and_download('UTTAR+PRADESH','BAGPAT',current_date,future_date)
find_and_download('UTTAR+PRADESH','BAHRAICH',current_date,future_date)
find_and_download('UTTAR+PRADESH','BALLIA',current_date,future_date)
find_and_download('UTTAR+PRADESH','BALRAMPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','BANDA',current_date,future_date)
find_and_download('UTTAR+PRADESH','BARABANKI',current_date,future_date)
find_and_download('UTTAR+PRADESH','BAREILLY',current_date,future_date)
find_and_download('UTTAR+PRADESH','BASTI',current_date,future_date)
find_and_download('UTTAR+PRADESH','BIJNOR',current_date,future_date)
find_and_download('UTTAR+PRADESH','BUDAUN',current_date,future_date)
find_and_download('UTTAR+PRADESH','BULANDSHAHR',current_date,future_date)
find_and_download('UTTAR+PRADESH','CHANDAULI',current_date,future_date)
find_and_download('UTTAR+PRADESH','CHITRAKOOT',current_date,future_date)
find_and_download('UTTAR+PRADESH','DEORIA',current_date,future_date)
find_and_download('UTTAR+PRADESH','ETAH',current_date,future_date)
find_and_download('UTTAR+PRADESH','ETAWAH',current_date,future_date)
find_and_download('UTTAR+PRADESH','FAIZABAD',current_date,future_date)
find_and_download('UTTAR+PRADESH','FARRUKHABAD',current_date,future_date)
find_and_download('UTTAR+PRADESH','FATEHPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','FIROZABAD',current_date,future_date)
find_and_download('UTTAR+PRADESH','GAUTAM+BUDDHA+NAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','GHAZIABAD',current_date,future_date)
find_and_download('UTTAR+PRADESH','GONDA',current_date,future_date)
find_and_download('UTTAR+PRADESH','GORAKHPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','HAMIRPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','HARDOI',current_date,future_date)
find_and_download('UTTAR+PRADESH','HATHRAS',current_date,future_date)
find_and_download('UTTAR+PRADESH','JALAUN',current_date,future_date)
find_and_download('UTTAR+PRADESH','JAUNPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','JHANSI',current_date,future_date)
find_and_download('UTTAR+PRADESH','JYOTIBA+PHULE+NAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','KANNAUJ',current_date,future_date)
find_and_download('UTTAR+PRADESH','KANPUR+DEHAT',current_date,future_date)
find_and_download('UTTAR+PRADESH','KANPUR+NAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','KAUSHAMBI',current_date,future_date)
find_and_download('UTTAR+PRADESH','KHERI',current_date,future_date)
find_and_download('UTTAR+PRADESH','KHUSHINAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','LALITPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','LUCKNOW',current_date,future_date)
find_and_download('UTTAR+PRADESH','MAHARAJGANJ',current_date,future_date)
find_and_download('UTTAR+PRADESH','MAHOBA',current_date,future_date)
find_and_download('UTTAR+PRADESH','MAINPURI',current_date,future_date)
find_and_download('UTTAR+PRADESH','MATHURA',current_date,future_date)
find_and_download('UTTAR+PRADESH','MAU',current_date,future_date)
find_and_download('UTTAR+PRADESH','MEERUT',current_date,future_date)
find_and_download('UTTAR+PRADESH','MORADABAD',current_date,future_date)
find_and_download('UTTAR+PRADESH','MUZAFFARNAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','PILIBHIT',current_date,future_date)
find_and_download('UTTAR+PRADESH','PRATAPGARH',current_date,future_date)
find_and_download('UTTAR+PRADESH','RAEBARELI',current_date,future_date)
find_and_download('UTTAR+PRADESH','RAMPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','SAHARANPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','SANT+KABIR+NAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','SANT+RAVIDAS+NAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','SHAHJAHANPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','SHRAWASTI',current_date,future_date)
find_and_download('UTTAR+PRADESH','SIDDHARTHNAGAR',current_date,future_date)
find_and_download('UTTAR+PRADESH','SITAPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','SONBHADRA',current_date,future_date)
find_and_download('UTTAR+PRADESH','SULTANPUR',current_date,future_date)
find_and_download('UTTAR+PRADESH','UNNAO',current_date,future_date)
find_and_download('UTTAR+PRADESH','VARANASI',current_date,future_date)

driver.quit()