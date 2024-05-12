from selenium import webdriver
from selenium.webdriver.common.by import By

from oopsDemo import oops

class childImp(oops):
    x = 20

    def getData(self):
        return self.x

    driver = webdriver.Chrome("//dfjflff")
    driver.get("fjsflsjfl")
    el = driver.find_element(By.ID, "fsdf")
    el.is_displayed()