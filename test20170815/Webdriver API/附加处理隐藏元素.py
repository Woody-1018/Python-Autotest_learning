
from selenium import webdriver
# 引入鼠标操作API
from selenium.webdriver.common.action_chains import ActionChains
import time

# driver = webdriver.Firefox()
# driver.get('https://www.baidu.com')
# # driver.maximize_window()
# element1 = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")
# ActionChains(driver).move_to_element(element1).perform()
# js = driver.find_element_by_xpath(".//*[@id='wrapper']/div[6]/a[1]").click()
# driver.execute_script(js)


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
search_setting = driver.find_element_by_xpath("//*[@id='u1']/a[8]")
ActionChains(driver).move_to_element(search_setting).perform()
time.sleep(3)
driver.find_element_by_css_selector("#wrapper > div.bdpfmenu > a.setpref").click()
driver.find_element_by_class_name("pfpanel").find_element_by_css_selector("#nr").click()




