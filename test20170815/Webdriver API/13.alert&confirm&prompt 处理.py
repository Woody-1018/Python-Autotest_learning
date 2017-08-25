from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
# # search_setting = driver.find_element_by_xpath("//*[@id='u1']/a[8]")
# search_setting = driver.find_element_by_css_selector("#u1 > a.pf")
# ActionChains(driver).move_to_element(search_setting).perform()
#
# driver.find_elements_by_xpath(".//*[@id='wrapper']/div[6]/a[2]").click()

search_setting = driver.find_elements_by_xpath("//*[@id='u1']/a[9]")
# ActionChains(driver).move_to_element(search_setting).perform()
driver.find_elements_by_xpath(".//*[@id='head']/div/div[4]/div/div[2]/div[1]/div/a[3]/span").click()





time.sleep(3)


