from selenium import webdriver
from Login import UserLogin
import time

driver = webdriver.Chrome()
driver.get("http://localhost/zentaopms/www/")
driver.maximize_window()
UserLogin.login(driver)
time.sleep(3)
UserLogin.logout(driver)

