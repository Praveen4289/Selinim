from selenium import webdriver
from selenium.webdriver.firefox.service import Service


s=Service(executable_path="C:\\Selenium drivers\\Firefox\\geckodriver.exe")
driver=webdriver.Firefox(service=s)
driver.get("http://www.instagram.com")
driver.minimize_window()
driver.maximize_window()



