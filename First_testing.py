from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.find_element(By.NAME,"email").send_keys("djbchjdb")
driver.find_element(By.NAME,"pass").send_keys("xcsdv")
driver.find_element(By.NAME,"login").click()