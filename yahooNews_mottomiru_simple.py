

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import lxml
import lxml.html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


#driver = webdriver.Chrome()
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
    
    
    # 最下部前スクロールしたければPAGE_DOWNを繰り返す
    body = driver.find_element(By.TAG_NAME, 'body')
    body.click()
    body.send_keys(Keys.PAGE_DOWN)

        
    time.sleep(3)
    driver.execute_script("arguments[0].click();", link_elem[0])
    time.sleep(3)
    
    page+=1
    print(page)

