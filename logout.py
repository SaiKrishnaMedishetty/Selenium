from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Wait for the elements to load
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH,"//*[@id='username']").send_keys("tomsmith")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH,"//*[@id='login']/button/i").click()
logout = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div/a/i")))
logout.click()

try:
    info = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div/h2")))
    message =info.text
    print(message)
    print("Everything is OK")
    input("enter")
except:
    print("something went wrong")