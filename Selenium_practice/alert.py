import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()

xpath = "//button[text()='Click for JS Alert']"

driver.find_element(By.XPATH, xpath).click()
time.sleep(3)

alert = driver.switch_to.alert
print(alert)


alert_text = alert.text
print(alert_text)

alert.accept()

driver.quit()
