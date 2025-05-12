from selenium import webdriver
import time

driver=webdriver.Edge()
driver.get('https://www.baidu.com')
time.sleep(2)
driver.close()