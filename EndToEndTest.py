import time

import requests
from numpy.ma import count
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.get("https://www.amazon.in/")
time.sleep(4)
el = driver.find_element(By.LINK_TEXT, "Facebook")
action = ActionChains(driver)
action.move_to_element(el).perform()
sourceElement = driver.find_element(By.XPATH, "xpath")
targetElement = driver.find_element(By.XPATH, "xpath")
action.drag_and_drop(sourceElement, targetElement).perform()
alert = driver.find_element(By.XPATH, "xpath")
driver.switch_to.alert
handels = driver.window_handles
driver.switch_to.window(handels)
el.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 5, poll_frequency=5, ignored_exceptions="NoElementException")
driver.execute_script(("arguments[0].setAttribute('value', 'text'')", el))
#check web page load time
#driver.set_page_load_timeout(7)

#disable ui blocker notifications
#option = Options()
#option.add_argument("--disable-notifications")
#driver = webdriver.Chrome(service=servObj, options = option)
# driver = webdriver.Chrome(service=servObj)
#
# driver.get("https://www.homedepot.com/")

#find the hieght, width, x and y coordinates of an element, we can use rect property
# val = driver.find_element(By.ID, "twotabsearchtextbox").rect
# print(val.get("width"))
time.sleep(8)
driver.close()


