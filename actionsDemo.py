import time
from webbrowser import Error

import document
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.fullscreen_window()
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# #action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).perform()

# print(driver.get_cookie(name="Ranju"))
# time.sleep(5)

# time.sleep(120)
# driver.close()



