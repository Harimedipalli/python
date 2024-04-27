import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
#
# alert = driver.switch_to.alert
# alert.accept()
# alert.send_keys("enter input to dailogue box")
#
# # windows
# main_window = driver.current_window_handle
# # Perform action to open new window
# new_window = driver.window_handles[1]
# driver.switch_to.window(new_window)




driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
WebDriverWait(driver, 10)
# time.sleep(10)
driver.implicitly_wait(10)

new_win = "//a[@href='/windows/new']"

# first window
driver.find_element(By.XPATH, new_win).click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

#second window
driver.find_element(By.XPATH, new_win).click()
driver.switch_to.window(driver.window_handles[0])

# third
driver.find_element(By.XPATH, new_win).click()
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

WebDriverWait(driver,10).until(EC.number_of_windows_to_be(4))


# driver.switch_to.window(driver.window_handles[3])
wind = driver.window_handles
print(wind)

driver.switch_to.window(wind[3])
time.sleep(2)
