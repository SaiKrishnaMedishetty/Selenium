from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.find_element(By.NAME,"email").send_keys("saik3651@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("Abhi@7711")
driver.find_element(By.NAME,"login").click()