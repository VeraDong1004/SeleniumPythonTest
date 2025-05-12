#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Edge()
driver.get('https://www.imooc.com')
driver.save_screenshot('tets.png')
time.sleep(2)

driver.close()