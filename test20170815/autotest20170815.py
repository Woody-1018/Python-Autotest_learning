#coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 定义浏览器
browser = webdriver.Chrome()
# 打开网页
browser.get('http://localhost/ranzhi/www/sys/user-login.html')
# 最大化窗口
browser.maximize_window()
# 清空输入框
browser.find_element_by_id("account").clear()
# 输入用户名
browser.find_element_by_id("account").send_keys("admin")
# 清空输入框
browser.find_element_by_id("password").clear()
# 输入密码
browser.find_element_by_id("password").send_keys("123456")
# 提交数据
browser.find_element_by_id("submit").click()

time.sleep(5)

# 获取title信息,并打印
title = browser.title
print(title)

# title断言
if title == "然之协同":
    print("title is ok")

else:
    print("title is wrong")

# 获取URL信息，并打印
current_page_url = browser.current_url
print(current_page_url)
# url断言
if current_page_url == "http://localhost/ranzhi/www/sys/index.html":
    print("url is ok")
else:
    print("url is wrong")

# 获取当前登录用户信息，并打印
login_user = browser.find_element_by_xpath("//*[@id='mainNavbar']/div/ul[1]/li/a").text
print(login_user)

time.sleep(5)
browser.quit()
