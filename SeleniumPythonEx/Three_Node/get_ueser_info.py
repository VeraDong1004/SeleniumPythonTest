#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge()
driver.get('https://www.imooc.com/user/newlogin')
time.sleep(2)
user_name_element=driver.find_element(By.NAME,'email')
print(user_name_element.get_attribute('placeholder'))
print(user_name_element.get_attribute('value'))
time.sleep(2)
user_name_element.send_keys('17360138091')
#当输入成功后，参数提示值并不会改变；可以查看新输入的值确认是否成功输入
print(user_name_element.get_attribute('value'))
time.sleep(2)

driver.close()