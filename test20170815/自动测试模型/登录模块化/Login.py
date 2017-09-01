
class UserLogin(object):

    @staticmethod
    def login(driver):
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("WuQi19901018")
        driver.find_element_by_id("submit").click()

    @staticmethod
    def logout(driver):
        driver.find_element_by_xpath(".//*[@id='topnav']/a[1]").click()
        driver.quit()




