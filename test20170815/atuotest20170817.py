# coding = utf-8
from selenium import webdriver
#输入鼠标API
from selenium.webdriver.common.action_chains import ActionChains
#输入键盘API
from selenium.webdriver.common.keys import Keys
#driver.find_element_by_id().send_keys(Keys.SPACE)
#driver.find_element_by_xpath().send_keys(Keys.BACK_SPACE)
#driver.find_element_by_xpath().send_keys(Keys.ENTER)
#driver.find_element_by_css_selector().send_keys(Keys.TAB)
#driver.find_element_by_css_selector().send_keys(Keys.CONTROL,'a')
#driver.find_element_by_name().send_keys(Keys.CONTROL,'c')
#driver.find_element_by_name().send_keys(Keys.CONTROL,'x')
#driver.find_elements_by_css_selector().send_keys(Keys.CONTROL,'v')
import time


driver = webdriver.Chrome()
first_url = "https://www.baidu.com"
second_url = "http://www.ifeng.com"
driver.get(first_url)
driver.maximize_window()
time.sleep(3)
driver.get(second_url)
driver.set_window_size(480,800)
time.sleep(3)
driver.maximize_window()
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.quit()