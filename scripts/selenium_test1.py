# coding:utf-8
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Safari()
browser.get('http://www.python.org')
assert 'Python' in browser.title
elem = browser.find_element_by_name('q')
elem.send_keys('pycon')

elem.submit() # 提交方法1
elem.send_keys(Keys.RETURN) # 模拟键盘回车
browser.find_element_by_id('submit').click() # 提交方法2
browser.find_element(By.XPATH)
elem.clear() # 清除输入框的文本

print browser.page_source # 输出网页渲染后的源代码


# select
# from selenium.webdriver.support.ui import Select
# select = Select(browser.find_element_by_name('test'))
# select.all_selected_options
# select.options