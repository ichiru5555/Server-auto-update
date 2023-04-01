from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path=r'chromeのdriverの絶対パス')
driver.get('https://www.xfree.ne.jp/login/member.php')
action = webdriver.ActionChains(driver)
driver.find_element(By.NAME,"memberid").send_keys("メールアドレス")
driver.find_element(By.NAME,"user_password").send_keys("パスワード")
action.send_keys(Keys.ENTER).perform()
time.sleep(5)
driver.find_element(By.NAME,"action_user_server_update").click()
time.sleep(15)
driver.close()
