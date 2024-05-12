import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(service=servObj, options=opt)




driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)



