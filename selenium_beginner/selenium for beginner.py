from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.chrome_executable_path = "/Users/louislin/Python/selenium_beginner/chromedriver"

driver = webdriver.Chrome(options=options)
url = 'https://www.ptt.cc/bbs/PC_Shopping/index.html'
driver.get(url)
search = driver.find_element(By.NAME, 'q')
search.send_keys('比特幣')
search.send_keys(Keys.RETURN)

titles = driver.find_element(By.LINK_TEXT, 'Re: [情報] 四川凌晨突襲礦場斷電 比特幣算力下跌34%')
titles.click()
driver.back()

time.sleep(5)
driver.quit()
