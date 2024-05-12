from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
openWindows = driver.window_handles

driver.switch_to.window(openWindows[1])

print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(openWindows[0])
assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"