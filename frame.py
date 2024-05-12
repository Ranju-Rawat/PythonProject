import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Ranju Rawat")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(5)
driver.close()