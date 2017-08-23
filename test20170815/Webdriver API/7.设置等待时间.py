# sleep()：设置固定休眠时间。python 的 time 包提供了休眠方法 sleep() ，导入 time 包后就可以使用 sleep()
# 进行脚本的执行过程进行休眠。
# implicitly_wait()：是 webdirver 提供的一个超时等待。隐的等待一个元素被发现，或一个命令完成。
# 如果超出了设置时间的则抛出异常。
# WebDriverWait()：同样也是 webdirver 提供的方法。在设置时间内，默认每隔一段时间检测一次当前
# 页面元素是否存在，如果超过设置时间检测不到则抛出异常。

# implicitly_wait()
# implicitly_wait()方法比 sleep() 更加智能，后者只能选择一个固定的时间的等待，前者可以在一个时间
# 范围内智能的等待。
# WebDriverWait()
# 详细格式如下：
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
# driver - WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
# timeout - 最长超时时间，默认以秒为单位
# poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
# ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
# 示例
# from selenium.webdriver.support.ui import WebDriverWait
# ....
# element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(“someId”))
# is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).
# until_not(lambda x: x.find_element_by_id(“someId”).is_displayed())

from selenium import webdriver
# 导入 WebDriverWait 包
from selenium.webdriver.support.ui import WebDriverWait
import time

# 定义浏览器
driver = webdriver.Chrome()
# 打开百度
driver.get("https://www.baidu.com")
# 固定等待时间
time.sleep(3)
driver.find_element_by_id("kw").send_keys("Selenium")
driver.quit()

# 定义浏览器
driver = webdriver.Chrome()
# 打开百度
driver.get("https://www.baidu.com")
# 智能等待时间
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys("Selenium")
driver.quit()

# 定义浏览器
driver = webdriver.Chrome()
# 打开百度
driver.get("https://www.baidu.com")
# WebDriverWait等待时间
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("kw"))
element.send_keys("Selenium")
driver.quit()
