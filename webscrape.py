from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PyPDF2 import PdfMerger
import time
import os
import time
import pickle

names = ['Pelosi','Greene','Khanna'] # Politicians used



driver = webdriver.Chrome(service=Service(r'C:\Users\ayden\Documents\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe'))  # Optional argument, if not specified will search path.

driver.get("https://disclosures-clerk.house.gov/PublicDisclosure/FinancialDisclosure")

time.sleep(5) # Let the user actually see something!

Search_reports = driver.find_element(By.LINK_TEXT, 'Search') 

Search_reports.click()

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element(By.ID, 'LastName')

for name in names:
    # Enter the search string

    search_box.clear()
    search_box.send_keys(name)

    # Wait for the page to load
    time.sleep(2)

    #Selects 2024 for the drop down
    select = Select(driver.find_element(By.ID, 'FilingYear'))
    select.select_by_visible_text('2024')
    time.sleep(1)
    
    # Submit the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(2)

time.sleep(5) # Let the user actually see something!


driver.quit()


