from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.chrome_executable_path = "/Users/louislin/PycharmProjects/selenium_tutorial/chromedriver"
driver = webdriver.Chrome(options=options)
driver.get("https://ca.linkedin.com/jobs/search?keywords=engineer&location=North%20York%2C%20Ontario%2C%20Canada&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0")
n=0
while n<3:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    n+=1
    titleTags=driver.find_elements(By.CLASS_NAME,"base-search-card__title")
for titleTag in titleTags:
    print(titleTag.text)
driver.close()