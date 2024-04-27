"""
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

shopping app : https://www.demoblaze.com/index.html

formy site for all operations : https://formy-project.herokuapp.com/

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://formy-project.herokuapp.com/")
# driver.maximize_window()

driver.implicitly_wait(5)

check_box = "//a[@class='btn btn-lg' and text()='Checkbox']"

time.sleep(3)

driver.find_element(By.XPATH, check_box).click()
time.sleep(2)

check_01 = '//input[@id="checkbox-1"]  '

driver.find_element(By.ID, "checkbox-1").click()
time.sleep(2)

check_02 = '//input[@id="checkbox-2"]'

driver.find_element(By.XPATH, check_02).click()
time.sleep(2)

check_03 = '//input[@id="checkbox-3"]'

driver.find_element(By.XPATH, check_03).click()
time.sleep(2)
