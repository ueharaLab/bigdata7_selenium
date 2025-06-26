

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import lxml
import lxml.html
from selenium import webdriver


driver = webdriver.Chrome()
#暗黙的な待機時間を設定する
driver.implicitly_wait(5)

key_word = input('key word:') #4740
driver.get('https://news.yahoo.co.jp/')

time.sleep(3)
driver.maximize_window() 
time.sleep(5)
elem = driver.find_elements(By.NAME,"p")
elem[2].send_keys(key_word)
elem[2].submit()


def page_scrape(html):    
    root = lxml.html.fromstring(html)
    article = root.xpath("//ol[@class='newsFeed_list']/li/*")
        
    for ar in article:        
        print(ar.text_content())
    
html = driver.page_source
page_scrape(html)

page =0   
while True:
   
    #<a class="more btn-more js-moreReview" data-id="4740" data-sort="" data-disp="10"><span>レビューをもっと見る</span></a>
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    link_elem=driver.find_elements(by=By.XPATH, value="//./span/button/span[text()='もっと見る']")   
    
    time.sleep(3)
    driver.execute_script("arguments[0].click();", link_elem[0])
    time.sleep(3)
        
    html = driver.page_source    
    page_scrape(html)  
        
    page+=1
    print(page)

