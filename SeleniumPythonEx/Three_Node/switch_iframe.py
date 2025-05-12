#coding=utf-8
from selenium import webdriver
from selenium.webdriver.commom.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Edge()
driver.get('https://www.imooc.com')
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
time.sleep(2)
'''进入提问页面，选择tag_name=iframe的元素框'''
driver.get('https://www.imooc.com/wenda')
driver.switch_to.frame('test')
time.sleep(2)
p_element=driver.find_element(By.TAG_NAME,'test')
ActionChains(driver).move_to_element(p_element).click().send_keys('test').perform()