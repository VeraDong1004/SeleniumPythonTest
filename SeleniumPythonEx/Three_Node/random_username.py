#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver=webdriver.Edge()
driver.get('https://www.imooc.com/user/newlogin')
time.sleep(2)
user_name_element=driver.find_element(By.NAME,'email')
for i in range(5):
    user_name_test=''.join(random.sample('13018871820',8))+'@qq.com'
    i+=1
    print(user_name_test)
    user_name_element.send_keys(user_name_test)
    time.sleep(3)

driver.close()

