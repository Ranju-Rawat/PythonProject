#Pytest file should start from test_
import pytest

def test_first():
    print("first")

def test_firstProgrammCreditCard():
    print("Hello")


def test_secProgramm():
    print("Good morning")


def test_crossbrowser():
    print("browserData")

obj = Service("driver_path")
driver = webdriver.Chrome(service=obj)
driver.get("URL")
assert driver.title == "test"

driver.find_element(By.ID, "id").click()


