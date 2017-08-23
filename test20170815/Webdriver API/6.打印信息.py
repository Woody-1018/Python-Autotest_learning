# title
# 返回当前页面的标题
# current_url
# 获取当前加载页面的 URL

from selenium import webdriver
import time

# 定义浏览器
driver = webdriver.Chrome()
# 打开燃之
driver.get("http://localhost/ranzhi/www/sys/user-login.html")
# 以 id 定位
driver.find_element_by_id("account").clear()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("submit").click()
time.sleep(3)

# 获取当前页面title
title = driver.title
print(title)

if title == "然之协同":
    print("title 正确 %s" % title)
else:
    print("title 不正确 %s")

# 获取当前页面url
now_url = driver.current_url
print(now_url)

if now_url == "http://localhost/ranzhi/www/sys/index.html":
    print("url 正确 %s" % now_url)
else:
    print("url 不正确 %s")

# 获取当前登录用户
now_user = driver.find_element_by_css_selector("#mainNavbar > div > ul:nth-child(1) > li > a").text
print(now_user)

driver.quit()

