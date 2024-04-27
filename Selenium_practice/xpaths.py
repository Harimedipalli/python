
# //tagname[@attribute="value"]
#
#
#
# # child class followed by parent class is seperated by /
#
# //tagname[@attribute="value"]/dev[6]


from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(5)
driver.maximize_window()

title = driver.title
print(title)

assert "Instagram" in title

username = '//input[@name="username"]'
password = '//input[@type="password"]'
login = '//button[@type="submit"]'

# username = driver.find_element(By.XPATH, username)
username1 = driver.find_element(By.NAME, "username")
username1.send_keys("9182892556")

# password = driver.find_element(By.XPATH, password)++
password1 = driver.find_element(By.NAME, "password")
password1.send_keys("Harihari@5")

time.sleep(10)

login1  = driver.find_element(By.XPATH, login)
login1.click()
time.sleep(10)

