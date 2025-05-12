#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Edge()
driver.get('https://www.imooc.com/user/newlogin')

'''
输入用户名class:
xa-emailOrPhone ipt ipt-email js-own-namem

输入密码class:
ipt ipt-pwd js-loginPassword js-pass-pwd
登录class:
moco-btn moco-btn-red moco-btn-lg btn-full xa-login
'''
time.sleep(2)
driver.maximize_window()
driver.find_element(By.NAME,'email').send_keys('1301887182@qq.com')
driver.find_element(By.NAME,'password').send_keys('Vera@1125')
driver.find_element(By.CLASS_NAME,'moco-btn').click()
time.sleep(4)
#个人设置界面
driver.get('https://www.imooc.com/user/setbindsns')
time.sleep(2)
driver.find_element(By.CLASS_NAME,'js-bind').click()
time.sleep(2)
handle_windows=driver.window_handles
current_window=driver.current_window_handle
for i in handle_windows:
    if i !=current_window:
        driver.switch_to.window(i)
        ti=EC.title_contains('网站连接')
        if ti(driver)=='true':
            break
time.sleep(20)
driver.find_element(By.CLASS_NAME,'qr-change-logo').click()
time.sleep(2)
driver.close()



