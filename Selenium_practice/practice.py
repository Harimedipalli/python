from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# uplaod a file

file_inp = driver.find_element(By.XPATH, "inputfile")

file_inp.send_keys("location of file")

# download a file

chrome_options = webdriver.ChromeOptions()
perfs = {"download.default_directory": "path to download"}
chrome_options.add_experimental_option("perfs", perfs)
driver = webdriver.Chrome(chrome_options=chrome_options)


