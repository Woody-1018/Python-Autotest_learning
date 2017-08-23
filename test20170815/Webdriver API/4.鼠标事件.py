# ActionChains 类鼠标操作的常用方法：
#  context_click() 右击
#  double_click() 双击
#  drag_and_drop() 拖动
#  move_to_element() 鼠标悬停在一个元素上
#  click_and_hold() 按下鼠标左键在一个元素上

from selenium import webdriver
# 引入鼠标操作API
from selenium.webdriver.common.action_chains import ActionChains
import time

# 定义浏览器
driver = webdriver.Chrome()
# 打开燃之
driver.get("http://localhost/ranzhi/www/sys/user-login.html")
driver.find_element_by_xpath("//*[@id='account']").clear()
driver.find_element_by_xpath("//*[@id='account']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='password']").clear()
driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(3)
# 定义元素
right_click = driver.find_element_by_css_selector("#s-menu-1 > button > img")
# 右击
ActionChains(driver).context_click(right_click).perform()

driver.find_element_by_css_selector("#taskMenu > li:nth-child(1) > a").click()

# 定义浏览器
driver = webdriver.Chrome()
# 打开百度地图
driver.get("http://map.baidu.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id("sole-input").send_keys("平安国际金融中心")
time.sleep(3)
driver.find_element_by_id("search-button").click()
time.sleep(5)
double_click = driver.find_element_by_id("mask")
ActionChains(driver).double_click(double_click).perform()
time.sleep(3)
ActionChains(driver).double_click(double_click).perform()
time.sleep(3)
ActionChains(driver).double_click(double_click).perform()
time.sleep(3)







