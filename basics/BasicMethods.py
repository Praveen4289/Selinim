import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# get, maximize-window, minimize-window, back,forward,refresh
s=Service(executable_path="C:\\Selenium drivers\\Chrome win_32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.google.com")
time.sleep(3)
driver.maximize_window()
driver.get("http://www.fb.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
driver.close()

