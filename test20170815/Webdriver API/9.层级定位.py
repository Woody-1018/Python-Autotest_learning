# 在实际的项目测试中，经常会有这样的需求：页面上有很多个属性基本相同的元素 ，现在需要具体
# 定位到其中的一个。由于属性基本相当，所以在定位的时候会有些麻烦，这时候就需要用到层级定位。先
# 定位父元素，然后再通过父元素定位子孙元素。

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("http://localhost/zentaopms/www/user-login.html")

driver.find_element_by_id("account").clear()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("ASD!@#123")
driver.find_element_by_id("submit").submit()

# 自己定位方式
driver.find_element_by_id("userMenu").click()
driver.find_element_by_link_text("个人档案").click()

# 教程定位方式
# driver.find_element_by_id("userMenu").click()
# menu = driver.find_element_by_class_name("dropdown-menu").find_element_by_link_text("个人档案")
# ActionChains(driver).move_to_element(menu).perform()

# iframe 切换
driver.switch_to.frame("modalIframe")

driver.find_element_by_css_selector("#titlebar > div.actions > a").click()
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("wuqi@bis.com.cn")
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys("13510567980")
driver.find_element_by_id("verifyPassword").clear()
driver.find_element_by_id("verifyPassword").send_keys("ASD!@#123")

# 无法定位到提交按钮，应该是被挡住了，需要用其他方式定位

# Use Actions or JavascriptExecutor for making it to click.

# By Actions:
# WebElement element = driver.findElement(By("element_path"));
# Actions actions = new Actions(driver);
# actions.moveToElement(element).click().perform();

# By JavascriptExecutor:
# JavascriptExecutor jse = (JavascriptExecutor)driver;
# jse.executeScript("scroll(250, 0)"); // if the element is on top.
# jse.executeScript("scroll(0, 250)"); // if the element is on bottom.

# or
# JavascriptExecutor jse = (JavascriptExecutor)driver;
# jse.executeScript("arguments[0].scrollIntoView()", Webelement);

driver.find_element_by_id("submit").click()


# 切回原文
driver.switch_to.default_content()

# 定位不到#####

driver.find_element_by_class_name("modal-content").find_element_by_class_name("close").click()














