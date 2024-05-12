import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(3)
#driver.find_element(By.LINK_TEXT, "India").click()
list = driver.find_elements(By.CLASS_NAME, "ui-menu-item")
print(len(list))
for item in list:
    if item.text == "India":
        item.click()
        break
    print(item.text)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


time.sleep(7)