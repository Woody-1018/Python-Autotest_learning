# 经常使用到的键盘操作：
# send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# send_keys(Keys.SPACE) 空格键(Space)
# send_keys(Keys.TAB) 制表键(Tab)
# send_keys(Keys.ESCAPE) 回退键（Esc）
# send_keys(Keys.ENTER) 回车键（Enter）
# send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
from selenium import webdriver
# 引入键盘操作API
from selenium.webdriver.common.keys import Keys
import time

# 定义浏览器
driver = webdriver.Chrome()
# 打开燃之
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium")
time.sleep(3)
# 删除键
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)
# 空格键
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(3)

driver.find_element_by_id("kw").send_keys("教程")
time.sleep(3)
# 制表键
driver.find_element_by_id("kw").send_keys(Keys.TAB)
time.sleep(3)
# 全选
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
# 复制
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'c')
time.sleep(3)
# 剪切
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)
# 粘贴
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
time.sleep(3)
# Enter键
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
driver.quit()




