#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from pykeyboard import PyKeyboard


'''
#打开慕课网主页并点击登录
driver=webdriver.Edge()
driver.get('https://www.imooc.com')
time.sleep(2)
#关闭弹窗
driver.find_element(By.ID,'js-advpop-close').click()
time.sleep(2)
element=driver.find_element(By.ID,'js-signin-btn')
element.click()
time.sleep(2)
#输入正确的用户名密码并登录
user_name=driver.find_element(By.NAME,'email')
user_name.send_keys('17360138090')
user_pwd=driver.find_element(By.NAME,'password')
user_pwd.send_keys('Vera@1125')
signin=driver.find_element(By.CLASS_NAME,'moco-btn')
signin.click()
time.sleep(5)
#进入个人设置界面并点击修改头像
driver.get('https://www.imooc.com/user/setprofile')
time.sleep(5)
#input类型标签-上传文件
driver.find_element(By.ID,'upload').send_keys('E:/哪吒壁纸合集/微信图片_20250211194048.jpg')
time.sleep(5)
driver.find_elements(By.CLASS_NAME,'moco-btn')[0].click()
'''

#非input类型标签-上传文件
driver=webdriver.Edge()
driver.get('https://chat.baidu.com/search')
pykey=PyKeyboard()
#切换输入法
pykey.tap_key(pykey.shift_key)
time.sleep(5)
pykey.type_string('E:\\test0314\\0314.jpg')
time.sleep(2)
pykey.tap_key(pykey.enter_key)
time.sleep(5)

driver.close()