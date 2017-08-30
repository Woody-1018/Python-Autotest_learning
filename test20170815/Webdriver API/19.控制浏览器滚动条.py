from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(1)
driver.get_screenshot_as_file("C:\\desktop\\baidu.png")
