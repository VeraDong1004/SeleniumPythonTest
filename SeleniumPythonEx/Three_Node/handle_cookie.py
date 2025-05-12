#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get('https://order.imooc.com/myorder')
time.sleep(5)
driver.delete_all_cookies()


'''
driver.get('https://www.imooc.com')
time.sleep(2)
#关闭弹窗
driver.find_element(By.ID,'js-advpop-close').click()
element=driver.find_element(By.ID,'js-signin-btn')
element.click()
time.sleep(2)

user_name=driver.find_element(By.NAME,'email')
user_name.send_keys('17360138090')
user_pwd=driver.find_element(By.NAME,'password')
user_pwd.send_keys('Vera@1125')
signin=driver.find_element(By.CLASS_NAME,'moco-btn')
signin.click()
time.sleep(5)
#获取cookies信息
cookies_lists=driver.get_cookies()
'''

cookie={'domain': '.imooc.com',
        'expiry': 1743493957,
        'httpOnly': False,
        'name': 'apsid',
        'path': '/',
        'sameSite': 'Lax',
        'secure': False,
        'value': 'IwNDI4MmRhZjhiOWM0YzNmZGFkMzU3OWZlMmQ0ZDMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjgyNTc2MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxMzAxODg3MTgyQHFxLmNvbQAAAAAAAAAAAAAAAAAAADI3YTkxOTQ0OGNlY2Y1NDMyZjI1ZGE4NGI2OTAyNGIywmDiZ8Jg4mc%3DNj'}
time.sleep(2)
driver.add_cookie(cookie)
time.sleep(2)
driver.get('https://order.imooc.com/myorder')
time.sleep(3)
driver.close()