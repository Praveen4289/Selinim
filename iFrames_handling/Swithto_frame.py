from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="D:/SeleniumDrivers/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)

page_text=driver.find_element(By.XPATH,"//a[@title='Lightning fast free email']").text
print(page_text)

# 1st way frame name or id
#driver.switch_to.frame("moneyiframe")

#2nd way frame index
#driver.switch_to.frame(0)

#3rd way  webelement
f=driver.find_element(By.XPATH,"//iframe[@title='Rediff Money Widget']")
driver.switch_to.frame(f)

frame_text=driver.find_element(By.XPATH,"//span[text()='BSE']").text
print(frame_text)

driver.switch_to.default_content()

page_text1=driver.find_element(By.XPATH,"//a[contains(@title,'Live commentary ')]").text
print(page_text1)