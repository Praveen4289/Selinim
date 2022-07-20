from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opt=Options()
opt.add_argument("--disable-notifications")
s=Service(executable_path="C:\\Selenium drivers\\Chrome win_32\\chromedriver.exe")
driver=webdriver.Chrome(service=s,options=opt)
driver.get("http://www.justdial.com")
driver.maximize_window()
driver.implicitly_wait(30)
