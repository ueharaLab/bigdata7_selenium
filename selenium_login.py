from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import lxml
import lxml.html
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(5)


# Googleアクセス
driver.get('https://4travel.jp/')
time.sleep(3)

# ①'ログインはこちら' にカーソルを移動する
elem = driver.find_element(By. )
# ①上記をクリック

time.sleep(3)

# ②メールアドレスのボックスにカーソルを移動
elem = driver.find_element(By.)
# メールアドレスを入力
elem.send_keys('' )
time.sleep(3)
# ②パスワードのボックスにカーソルを移動
elem = driver.find_element(By.)
# パスワードを入力
elem.send_keys('')
# フォームを送信
elem.submit()
