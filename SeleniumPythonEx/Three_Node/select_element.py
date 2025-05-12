#coding=utf8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


'''打开慕课网主页并点击登录'''
driver=webdriver.Edge()
driver.get('https://www.imooc.com')
time.sleep(2)
#关闭弹窗
driver.find_element(By.ID,'js-advpop-close').click()
time.sleep(2)
element=driver.find_element(By.ID,'js-signin-btn')
element.click()
time.sleep(2)
'''输入正确的用户名密码并登录'''
user_name=driver.find_element(By.NAME,'email')
user_name.send_keys('17360138090')
user_pwd=driver.find_element(By.NAME,'password')
user_pwd.send_keys('Vera@1125')
signin=driver.find_element(By.CLASS_NAME,'moco-btn')
signin.click()
time.sleep(5)
'''进入个人设置界面并点击修改个人信息'''
driver.get('https://www.imooc.com/user/setprofile')
mod_info=driver.find_element(By.CLASS_NAME,'edit-info-btn')
mod_info.click()


#driver.find_elements(By.NAME,'job')[1].find_elements(By.TAG_NAME,'option')[1].click()
#select=driver.find_elements(By.NAME,'job')[1]
#Select(select).select_by_value('6')

driver.find_elements(By.CLASS_NAME,'moco-form-control')[11].find_elements(By.TAG_NAME,'option')[1].click()
time.sleep(2)
select_element=driver.find_elements(By.CLASS_NAME,'moco-form-control')[11]
Select(select_element).select_by_value('6')
time.sleep(2)
Select(select_element).select_by_index(5)
time.sleep(2)
Select(select_element).select_by_visible_text('UI设计师')

time.sleep(2)
driver.close()