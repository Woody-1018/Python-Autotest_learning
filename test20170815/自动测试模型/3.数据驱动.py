
from selenium import webdriver
import time

search_keywords = ['selenium', 'python', 'java', 'pycharm', '京东', '布加迪']

for search in search_keywords:
    browser = webdriver.Chrome()
    browser.get("https://www.baidu.com")
    browser.find_element_by_id("kw").send_keys(search)
    browser.find_element_by_id("su").click()

time.sleep(5)
