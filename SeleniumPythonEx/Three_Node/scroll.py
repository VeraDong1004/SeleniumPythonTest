#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge()
driver.get('https://imooc.com')
time.sleep(2)
#关闭弹窗
driver.find_element(By.ID,'js-advpop-close').click()
time.sleep(2)
#element=driver.find_elements(By.CLASS_NAME,'footer-link')[0].find_elements(By.TAG_NAME,'a')[4]
#element.click()

driver.get('https://www.imooc.com/wenda')
time.sleep(2)
js = 'document.documentElement.scrollTop=1000;'
#driver.execute_script(js)
t=True
while t:
    element_list = driver.find_elements(By.CLASS_NAME, 'que-con')
    for element in element_list:
        course_name=element.find_element(By.TAG_NAME,'a').text
        print(course_name)
        if course_name=="我现在的情况能找到工作吗？":
            element.click()
            t = False
    driver.execute_script(js)
    time.sleep(2)

driver.close()

