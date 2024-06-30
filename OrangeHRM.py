from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/")

# act_title = driver.title
# exp_title = "OrangeHRM"

# if act_title == exp_title:
#     print("test case is passed")
# else:
#     print("Failed")

###### linktext

# text = driver.find_element(By.LINK_TEXT,"Resources").click()


# if text is None:
#     print("passed")
# else:
#     print("Failed")

#Class

slides = driver.find_element(By.CLASS_NAME,"homepage-slider-bottom")
print(type(slides)) 

# print(len(slides))

driver.close()


