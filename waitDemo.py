import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servObj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
time.sleep(4)
#products = driver.find_elements(By.CSS_SELECTOR, ".product")
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products)
print(count)
assert count > 0

for prod in products:
    prod.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(5)
assert driver.find_element(By.CLASS_NAME, "promoInfo").text == "Code applied ..!"

#time.sleep(5)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "promoInfo")))

#xpath to get amount column - //td[5]

amounts = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//td[5]")))
sum = 0
for amount in amounts:
    if amount.text != "Total":
        print(amount.text)
        amt = int(amount.text)
        sum += amt
print("Total Amount", sum)

totAmt =  driver.find_element(By.CLASS_NAME, "totAmt").text
assert int(totAmt) == sum

discAmt = driver.find_element(By.CLASS_NAME, "discountAmt").text
assert float(discAmt) < int(totAmt)


driver.close()