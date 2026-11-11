"""ローカル NEWS LAB 用 Selenium 演習・教員用解答。"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import lxml.html
import time

key_word = 'AI'



def page_scrape(html, already_printed=0):
    root = lxml.html.fromstring(html)
    articles = root.xpath( "####")     # 記事本文のxpath
    for article in articles[already_printed:]:
        print(' '.join(article.text_content().split()))
    return len(articles)


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('####') # トップページのURL
driver.maximize_window()

time.sleep(5)
elem = driver.find_elements(By.NAME, '####')# 検索窓のフォームのname属性
elem[0].send_keys(key_word)
elem[0].submit()
time.sleep(3)

html = driver.page_source
count = page_scrape(html)

for page in range(5):
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

    link_elem = driver.find_elements(By.####,"####") # By, p.26 のカーソル移動仕様を参考に埋める
    
    time.sleep(3)
    driver.execute_script("arguments[0].click();", link_elem[0])
    time.sleep(3)

    html = driver.page_source
    count = page_scrape(html, count)
    print('クリック回数:', page + 1, '累計:', count, '件')

driver.quit()
