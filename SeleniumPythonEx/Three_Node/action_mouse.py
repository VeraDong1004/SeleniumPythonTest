#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get('https://imooc.com')
#关闭弹窗
driver.find_element(By.ID,'js-advpop-close').click()
time.sleep(2)

element=driver.find_element(By.CLASS_NAME,'menuContent').find_elements(By.CLASS_NAME,'item')[0]
ActionChains(driver).move_to_element(element).perform()
time.sleep(3)

element1=driver.find_elements(By.CLASS_NAME,'lores')[0].find_element(By.LINK_TEXT,'DeepSeek')
element1.click()
time.sleep(5)

driver.close()
