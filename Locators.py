import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

sObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=sObj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#locators in selenium - Id, xpath, cssSelector, classname, name, linktext, partialLinktext, tagname
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
# For static dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
driver.add_cookie({"name": "ranju", "value": "30"})
cookies = driver.get_cookies()
print("cookies",cookies)
delelteC = driver.delete_cookie("ranju")
print(cookies)

dropdown.select_by_index(0)

#dropdown.select_by_value("value")
dropdown.select_by_visible_text("Female")
#xpath = //tagname[@attribute = "value"]
driver.find_element(By.XPATH, "//input[@type='submit']").click()
msg = driver.find_element(By.CLASS_NAME, "alert-success").text

print(msg)
assert "success" in msg

#cssSelector = "tagname[attribute = 'value']", #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Ranju Rawat")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("Hellow again")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()
#driver.forward()


time.sleep(7)
driver.close()
