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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.implicitly_wait(5)


user_xpath = '//input[@name="username"]'
pass_xpath = '//input[contains(@name,"pass")]'
login_xpaths = '//button[@type="submit"]'
admin_xpath = '//span[text()="Admin"]'
user_role = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
toggle_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]"
search = '//button[text()=" Search "]'

username = driver.find_element(By.XPATH, user_xpath)
username.send_keys("Admin")

password = driver.find_element(By.XPATH, pass_xpath)
password.send_keys("admin123")

login = driver.find_element(By.XPATH, login_xpaths)
login.click()
time.sleep(3)

wait = WebDriverWait(driver,15)

admin = wait.until(EC.presence_of_element_located((By.XPATH, admin_xpath)))
admin.click()



# finding the toggle element
dropdown_toggle = driver.find_element(By.XPATH, toggle_xpath)
dropdown_toggle.click()

wait = WebDriverWait(driver, 20)
dropdown_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")))

for option in dropdown_options:
    print(option.text)
    if option.text == "Admin":  # Replace "SCC" with the text of the option you want to select
        option.click()
        break

time.sleep(10)

search_button = driver.find_element(By.XPATH, search)
search_button.click()
time.sleep(4)
job = "//ul//li//a[text()='Job Titles']"

dropdown_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul//li//a[@role='menuitem']")))

for opt in dropdown_options:
    print(opt.text)
    if opt.text=="Job Titles":
        opt.click()

time.sleep(3)
