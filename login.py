from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://the-internet.herokuapp.com/login")

# Maximize the window
driver.maximize_window()

# Wait until elements are present
wait = WebDriverWait(driver, 10)

# Enter Username
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("tomsmith")

# Enter Password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SuperSecretPassword!")

# Click the Login Button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Validate successful login by checking if the logout button is present
try:
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/logout']")))
    print("Login successful!")
except:
    print("Login failed!")

# Pause to observe before quitting
input("Press Enter to close the browser...")

# Close the browser
driver.quit()

