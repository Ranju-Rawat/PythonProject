import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")

driver = webdriver.Chrome(service=servObj, options=chrome_option)
driver.implicitly_wait(5)

#handle browser certificate err
#chrome_option.add_argument("--ignore certificate-errors")



driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")
driver.get_screenshot_as_png()

time.sleep(5)
driver.close()