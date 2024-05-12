import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serObj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    print(checkbox.get_attribute("value"))
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR, "input[value='Hide']").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


time.sleep(4)
driver.close()
