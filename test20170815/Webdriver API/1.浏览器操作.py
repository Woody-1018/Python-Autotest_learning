# coding = utf-8
# 引入WebDriver
from selenium import webdriver
# 引入计时器
import time
# 定义浏览器
driver = webdriver.Chrome()
# get方式打开链接
driver.get("https://www.baidu.com")
# 最大化窗口
driver.maximize_window()
# 浏览器刷新
driver.refresh()
# 等待时间
time.sleep(5)
# 打印信息
print("设置浏览器宽度为480，高度为800")
# 自定义窗口大小
driver.set_window_size(480, 800)
# 打印信息
print("设置浏览器宽度为480，高度为800")
# 等待时间
time.sleep(5)
# 退出浏览器（driver.close() 关闭当前窗口,不退出浏览器）
driver.quit()

# 定义变量
first_url = 'https://www.baidu.com'
second_url = 'http://www.163.com'
# 定义浏览器
driver = webdriver.Firefox()
# 打印信息
print("打开第一个地址 %s" % first_url)
# 打开第一个网页
driver.get(first_url)
# 打印信息
print("打开第二个地址 %s" % second_url)
# 打开第二个网页
driver.get(second_url)
# 打印信息
print("回退到第一个地址 %s" % first_url)
# 浏览器回退
driver.back()
# 打印信息
print("前进到第二个地址 %s" % second_url)
# 浏览器前进
driver.forward()
# 关闭窗口
driver.close()







