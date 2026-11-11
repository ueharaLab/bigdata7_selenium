"""教員用解答例。"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import lxml.html

URL = 'http://127.0.0.1:8000/'
KEYWORD = 'AI'  # このキーワードは60件ヒット（最初10件 + もっと見る5回）
MAX_CLICKS = 5

# ===== 穴埋め問題 =====
SEARCH_NAME = 'keyword'
ARTICLE_XPATH = '//ol[@class="story-list"]/li/article'
MORE_XPATH = '//div[@id="loadPanel"]/button[span[text()="もっと見る"]]'
# ======================

def page_scrape(html):
    root = lxml.html.fromstring(html)
    articles = root.xpath(ARTICLE_XPATH)
    print(f'現在の記事数：{len(articles)}')
    for article in articles[-10:]:
        print(' -', ' '.join(article.text_content().split()))
    return len(articles)

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(URL)
    elem = wait.until(EC.presence_of_element_located((By.NAME, SEARCH_NAME)))
    elem.send_keys(KEYWORD)
    elem.submit()
    wait.until(lambda d: len(lxml.html.fromstring(d.page_source).xpath(ARTICLE_XPATH)) >= 10)
    count = page_scrape(driver.page_source)
    for page in range(MAX_CLICKS):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        more = wait.until(EC.element_to_be_clickable((By.XPATH, MORE_XPATH)))
        driver.execute_script('arguments[0].click();', more)
        wait.until(lambda d: len(lxml.html.fromstring(d.page_source).xpath(ARTICLE_XPATH)) > count)
        count = page_scrape(driver.page_source)
        print(f'クリック{page + 1}回目：{count}件を表示\n')
    assert count == 60, f'想定と異なる件数: {count}'
    print('演習成功：5回の「もっと見る」で60件を表示できました！')
