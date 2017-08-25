from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 无法通过click获取登录窗口
# <a href="https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F"
# name="tj_login" class="lb" onclick="return false;">登录</a>
driver.find_element_by_name("tj_login").click()
time.sleep(5)
driver.find_element_by_id("TANGRAM__PSP_10__userName").clear()
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("wuqi19901018")
driver.find_element_by_id("TANGRAM__PSP_10__password").clear()
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("wuqi19901018")