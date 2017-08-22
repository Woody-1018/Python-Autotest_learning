from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https:/www.baidu.com")
driver.maximize_window()
search_set = driver.find_element_by_name("tj_settingicon")
ActionChains(driver).move_to_element(search_set).perform()
driver.find_element_by_xpath("//div[class='bdpfmenu']/a[1]").click()

time.sleep(5)
driver.quit()
# driver.find_elements_by_link_text("搜索设置").click()

