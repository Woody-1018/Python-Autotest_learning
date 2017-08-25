# find_elements_by
# 定位一组对象一般用于以下场景：
#  批量操作对象，比如将页面上所有的 checkbox 都勾上
#  先获取一组对象，再在这组对象中过滤出需要具体定位的一些对象。比如定位出页面上所有的
# checkbox，然后选择最后一个

from selenium import webdriver
# os 模块为 python 语言标准库中的 os 模块包含普遍的操作系统功能。主要用于操作本地目录文件。
# path.abspath()方法用于获取当前路径下的文件。另外脚本中还使用到 for 循环，对 inputs 获取的一组元素
# 进行循环，在 python 语言中循环变量（input）可以不用事先声明直接使用。
import os
import time
driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("checkbox.html")
driver.get(file_path)
checkbox = driver.find_elements_by_tag_name("input")
time.sleep(3)
for checkbox in checkbox:
    if checkbox.get_attribute("type") == "checkbox":
        checkbox.click()
time.sleep(3)

# 打印checkbox 数量
print(len(driver.find_elements_by_tag_name("input")))

# 取消勾选最后一个复选框
driver.find_elements_by_tag_name("input").pop().click()

time.sleep(3)

driver.quit()
