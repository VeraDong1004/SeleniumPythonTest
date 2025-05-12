#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


driver=webdriver.Edge()
time.sleep(2)
driver.get('https://www.imooc.com')
time.sleep(2)
driver_title=EC.title_contains('慕课网')
print(driver_title(driver))

locator=(By.CLASS_NAME,'icon-shopping-cart')
a=WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
print(a)
driver.close()



