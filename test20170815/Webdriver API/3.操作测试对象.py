# webdriver 中比较常用的操作元素的方法有下面几个：
#  clear 清除元素的内容，如果可以的话
#   用于清除输入框的默认内容
#  send_keys 在元素上模拟按键输入
#  click 单击元素
#  submit 提交表单

# WebElement 接口常用方法

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 获取元素尺寸
size = driver.find_element_by_id("kw").size
print(size)

# 获取元素文本信息
text = driver.find_element_by_id("cp").text
print(text)

# 获取元素属性
attribute = driver.find_element_by_id("su").get_attribute('type')
print(attribute)
attribute = driver.find_element_by_id("su").get_attribute('value')
print(attribute)
attribute = driver.find_element_by_id("su").get_attribute('class')
print(attribute)

# 设置该元素是否用户可见
display = driver.find_element_by_id("cp").is_displayed()
print(display)



