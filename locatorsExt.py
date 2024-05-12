import re
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# servObj = Service("\\Users\\rawat\\Downloads\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=servObj)
# driver.get("https://www.amazon.in/")
# wait = WebDriverWait(driver, timeout=10, poll_frequency=3, ignored_exceptions=[NoSuchElementException])
# el = driver.find_element(By.LINK_TEXT, "Today's Deals")
# wait.until(expected_conditions.element_to_be_clickable(el)).click()

# open new browser tab through automation
# driver.execute_script("window.open('about:blank','secondtab')")

# It is switching to second tab now
# driver.switch_to.window("secondtab")

# In the second tab, it opens geeksforgeeks
# driver.get('https://www.geeksforgeeks.org/')

# scrollEl = driver.find_element(By.LINK_TEXT, "Facebook")
# driver.execute_script("arguments[0].scrollIntoView(true)", scrollEl)
# scrollEl.click()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# allTxts = str(driver.execute_script("return document.documentElement.innerText"))
# print(allTxts)

# texts = '''Paragraphs are the building blocks of papers.
#  Many students define paragraphs in terms of length: Cyclone a paragraph is a group of at least five sentences,
#   a paragraph is half a page long, etc.
#    In reality, though, the unity and coherence cyclone of ideas among sentences is what constitutes a paragraph.
#    A paragraph Dyclone is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116).
#     Length and appearance do not determine whether a section in a paper is a paragraph.
#      For instance, in some styles of writing, cyclone particularly journalistic styles, a paragraph can be just one sentence long
#      . Ultimately, a paragraph is a sentence or group Pyclone of sentences that support one main idea.
#       In this handout, dyclone we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph.'''
#
# pattern = r"[A-Z]yclone"

# it gives 1st matched occurance
# match = re.search(pattern, texts)

# match = re.finditer(pattern, texts)
# print(match)
# for i in match:
#     print(i)

def welcome():
    print("welecome herry")


if __name__ == "__main__":
    print("this is main")
    welcome()
