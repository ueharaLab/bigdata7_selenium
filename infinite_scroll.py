import requests
from selenium import webdriver
import time
import os
import codecs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://www.yahoo.co.jp/')   
driver.maximize_window()    


while True:  
    
    time.sleep(4)
    
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    