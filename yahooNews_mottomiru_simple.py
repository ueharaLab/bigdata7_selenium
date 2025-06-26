

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import lxml
import lxml.html
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(5)

key_word = input('key word:') #4740

driver.get('https://news.yahoo.co.jp/search?p={}&ei=utf-8/'.format(key_word))
time.sleep(3)
driver.maximize_window() 
time.sleep(5)
page =0   
while True:  
    
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    link_elem=driver.find_elements(by=By.XPATH, value="//./span/button/span[text()='もっと見る']")   
    
    time.sleep(3)
    driver.execute_script("arguments[0].click();", link_elem[0])
    time.sleep(3)
    
    page+=1
    print(page)

