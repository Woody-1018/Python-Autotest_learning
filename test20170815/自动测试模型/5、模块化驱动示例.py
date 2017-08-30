from selenium import webdriver
import time
# driver = webdriver.Chrome()
# driver.get("http://localhost/zentaopms/www/")
# driver.maximize_window()
# driver.find_element_by_name("account").clear()
# driver.find_element_by_name("account").send_keys("admin")
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys("WuQi19901018")
# driver.find_element_by_id("submit").click()
# driver.find_element_by_css_selector("#mainmenu > ul > li:nth-child(4) > a").click()
# driver.find_element_by_link_text("用例").click()
# driver.find_element_by_css_selector("#createActionMenu > a").click()
# driver.find_element_by_css_selector("#type_chosen > a > span").click()
# driver.find_element_by_css_selector("#type_chosen > a > span").click()
# # .//*[@id='topnav']/a[1]
# # driver.find_elements_by_css_selector("#topnav > a:nth-child(2)").click()
# driver.find_element_by_xpath(".//*[@id='topnav']/a[1]").click()
#
# driver.quit()


def login():
    driver.find_element_by_name("account").clear()
    driver.find_element_by_name("account").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("WuQi19901018")
    driver.find_element_by_id("submit").click()


def logout():
    driver.find_element_by_xpath(".//*[@id='topnav']/a[1]").click()
    driver.quit()

driver = webdriver.Chrome()
driver.get("http://localhost/zentaopms/www/")
driver.maximize_window()
login()
logout()
