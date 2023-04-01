from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path=r'chromeのdriverの絶対パス')
driver.get('https://secure.netowl.jp/netowl/?service=starserver')
action = webdriver.ActionChains(driver)
driver.find_element(By.NAME,"mailaddress").send_keys("メールアドレス")
driver.find_element(By.NAME,"password").send_keys("パスワード")
action.send_keys(Keys.ENTER).perform()
time.sleep(15)
driver.find_element(By.XPATH,"//*[contains(text(), '無料プラン管理')]").click()
driver.find_element(By.CSS_SELECTOR, "input[value='無料更新']").click()
time.sleep(20)
driver.find_element(By.XPATH,"//*[contains(text(), 'ログアウト')]").click()
driver.close()
