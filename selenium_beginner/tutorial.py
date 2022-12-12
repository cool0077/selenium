from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.chrome_executable_path = "/Users/louislin/PycharmProjects/selenium_tutorial/chromedriver"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot-google.png")
driver.get("https://www.ntu.edu.tw/")
driver.save_screenshot("screenshot-ntu.png")
driver.close()