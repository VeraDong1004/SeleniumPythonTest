#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import sys
sys.path.append('E:\\00-PycharmProjects\\SeleniumPythonEx')
from Three_Node.read_init import read_ini

class FindElement():
    def __init__(self,driver):
        self.driver=driver

    def get_local_element(self,key):
        '''通过读取文件中的值定位元素'''
        data = read_ini.get_value1(key)
        data_info = data.split('>')
        return data_info

    def get_element1(self,key):
        '''获取元素'''
        element = None
        by,Value = self.get_local_element(key)
        try:
            if by == 'id':
                element = self.driver.find_element(By.ID, Value)
            elif by == 'name':
                element = self.driver.find_element(By.NAME, Value)
            elif by == 'class':
                element = self.driver.find_element(By.CLASS_NAME, Value)
            elif by == 'css':
                element = self.driver.find_element(By.CSS_SELECTOR, Value)
            else:
                element = self.driver.find_element(By.XPATH, Value)
        finally:
            return element


if __name__=='__main__':
    driver=FindElement('edge')
    print(driver.get_element1('username'))