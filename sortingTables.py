import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
vegList = driver.find_elements(By.XPATH, "//tr/td[1]")
vegies = []
for veg in vegList:
    vegies.append(veg.text)

print(vegies)
newList = vegies.copy()

newList.sort()
print(newList)
assert newList == vegies