from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the button to trigger an alert
driver.find_element("xpath", "//button[text()='Click for JS Alert']").click()

# Switch to alert and accept it
alert = driver.switch_to.alert
print("Alert Text:", alert.text)  # Print alert text
alert.accept()  # Click OK

# If it's a confirmation alert with "OK" and "Cancel"
# alert.dismiss()  # Click Cancel

# If it's a prompt alert where you can enter text
# alert.send_keys("Hello")  # Enter text in alert
# alert.accept()

driver.quit()
