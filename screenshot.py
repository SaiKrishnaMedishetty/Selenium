from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://the-internet.herokuapp.com/login")

# Maximize window
driver.maximize_window()

# Wait for the elements to load
wait = WebDriverWait(driver, 10)

# Enter Invalid Username
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("wronguser")

# Enter Invalid Password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("wrongpassword")

# Click the Login Button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Verify Error Message
try:
    error_message = wait.until(EC.presence_of_element_located((By.ID, "flash")))
    print("Error Message Displayed: ", error_message.text)

    # Capture Screenshot
    driver.save_screenshot("invalid_login_error.png")
    print("Screenshot saved as 'invalid_login_error.png'")
except:
    print("Error message not found!")

# Pause for observation
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
