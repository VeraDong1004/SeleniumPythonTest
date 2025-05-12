#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as  EC
import time
driver=webdriver.Edge()
driver.get('https://imooc.com')
time.sleep(3)
title_name=driver.title
if '慕课网' in title_name:
    print('执行正确')
else:
    print('打开错误')


title_a=EC.title_is('慕课网') #完全等于
print(title_a(driver))
title_b=EC.title_contains('慕课网') #包含
print(title_b(driver))
driver.close()