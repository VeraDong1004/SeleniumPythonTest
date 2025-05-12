#coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get('https://imooc.com')
driver.maximize_window()
time.sleep(2)


'''find_element(By.lINK_TEXT):超链接'''
#driver.find_element(By.LINK_TEXT,'实战课').click()
#time.sleep(3)

'''css-selector定位：层级定位'''
#driver.find_element(By.ID,'js-signin-btn').click()
#time.sleep(2)
#driver.find_element(By.CSS_SELECTOR,'.rlf-group>.xa-emailOrPhone').send_keys('test')
#time.sleep(3)

'''find_element(By.CLASS_NAME)'''
#driver.find_element(By.CLASS_NAME,'shop-cart-icon').click()
#time.sleep(2)

windows_handles=driver.window_handles
current_window=driver.current_window_handle
for i in windows_handles:
    if i !=current_window:
        driver.switch_to.window(i)
#find_element(By.ID)
driver.find_element(By.ID,'js-signin-btn').click()
time.sleep(2)
#find_element(By.NAME)
element1=driver.find_element(By.NAME,'email')
element1.send_keys('1301887182@qq.com')
element2=driver.find_element(By.NAME,'password')
element2.send_keys('Vera@1125')
'''XPATH定位'''
driver.find_element(By.XPATH,"//body/div[@id='signin']/div[2]/div[1]/form[1]/div[5]/input[1]").click()
time.sleep(5)

driver.close()
