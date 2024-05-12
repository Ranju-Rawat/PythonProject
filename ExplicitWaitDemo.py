import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
time.sleep(4)
#products = driver.find_elements(By.CSS_SELECTOR, ".product")
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
#prodNm = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
count = len(products)
assert count > 0
expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []
for prod in products:
    nmList = prod.find_elements(By.XPATH, "h4")
    for nm in nmList:
        actualList.append(nm.text)

print("This is ExpectedList", expectedList)
print("This is actualList", actualList)
assert expectedList == actualList