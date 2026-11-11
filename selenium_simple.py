from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(5)

driver.get('https://www.yahoo.co.jp/')
driver.maximize_window() 
time.sleep(5)
# 検索ボックスを特定
elem = driver.find_element(By.NAME, 'p')
time.sleep(5)

elem.send_keys('ゴリラ')
time.sleep(5)
elem.send_keys(Keys.ENTER)
