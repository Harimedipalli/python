from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Chrome()

driver.get("https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv")

driver.maximize_window()


time.sleep(3)

xpath = "//a[contains(@href, 'addresses.csv')]"

driver.find_element(By.LINK_TEXT, 'addresses.csv').click()
WebDriverWait(driver, 30).until(EC.element_to_be_clickable)


file_path = "Downloads"

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
for row in csv_reader:
    print(row)
driver.quit()

