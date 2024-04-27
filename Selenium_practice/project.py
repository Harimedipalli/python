import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
title = driver.title
print(title)

assert "OrangeHRM" in title

# Xpaths
username = "//input[@name='username']"
password = "//input[@name='password']"
login = "//button[@type='submit']"

# uplaod a file
usname = driver.find_element(By.XPATH,username )
usname.send_keys("Admin")
passwod = driver.find_element(By.XPATH, password)
passwod.send_keys("admin123")
wait = WebDriverWait(driver, 10)

submit = driver.find_element(By.XPATH, login)
submit.click()
wait = WebDriverWait(driver, 10)
time.sleep(10)
# ele = wait.until(EC.element_to_be_clickable(By.XPATH))

leave = '//a[@class="oxd-main-menu-item active"]'
driver.find_element(By.XPATH, leave).click()



# my_info  = '//a[@class="oxd-main-menu-item active"]'
#
# driver.find_element(By.XPATH, my_info).click()
# time.sleep(3)
#
# driver.find_elements(By.LINK_TEXT, )




