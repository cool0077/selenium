from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.chrome_executable_path = "/Users/louislin/PycharmProjects/selenium_tutorial/chromedriver"
driver = webdriver.Chrome(options=options)
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
tags = driver.find_elements(By.CLASS_NAME, "title")
for tag in tags:
    print(tag.text)
link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click()
tags = driver.find_elements(By.CLASS_NAME, "title")
for tag in tags:
    print(tag.text)
driver.close()