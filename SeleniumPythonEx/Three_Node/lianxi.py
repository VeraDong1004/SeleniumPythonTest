#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
'''
driver=webdriver.Firefox()
driver.get('https://www.imooc.com/user/newlogin')
driver.maximize_window()
time.sleep(2)
username_ele=driver.find_element(By.NAME,'email')
username_ele.send_keys('123')

password_ele=driver.find_element(By.NAME,'password')
password_ele.click()
time.sleep(2)

username_error_ele=driver.find_element(By.XPATH,'//*[@id="signup-form"]/div[1]/p')
print(username_error_ele.get_attribute('textContent'))

password_ele.send_keys('123')
login_btn=driver.find_element(By.XPATH,'//*[@id="signup-form"]/div[5]/input')
login_btn.click()
time.sleep(2)

password_error_ele=driver.find_element(By.XPATH,'//*[@id="signup-form"]/div[2]/p')
print(password_error_ele.get_attribute('textContent'))

time.sleep(2)
driver.close()
'''