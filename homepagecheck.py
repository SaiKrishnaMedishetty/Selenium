from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://automationexercise.com")

try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
    print("yes")
except AssertionError:
    print("No")