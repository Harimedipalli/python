from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/')

print(browser.title)
try:
    assert "YouTube" == browser.title
except AssertionError:
    print(f'page tile is not found with expected title,Actuval title{browser.title}but expected title is {"YouTube"}')

browser.maximize_window()
time.sleep(5)
browser.minimize_window()
time.sleep(5)
browser.maximize_window()
time.sleep(5)
browser.minimize_window()
time.sleep(5)
browser.close()




