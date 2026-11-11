import requests
from selenium import webdriver
import time
import os
import codecs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
chrome_options = Options()
options.add_argument('--headless')
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.yahoo.co.jp/')   
driver.maximize_window()    


while True:  
    
    time.sleep(4)
    
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    