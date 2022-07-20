import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path="C:\\Selenium drivers\\Chrome win_32\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.instagram.com")
driver.minimize_window()
time.sleep(3)
driver.maximize_window()



