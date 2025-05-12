#coding=utf-8
from selenium import webdriver
from base.login_get_element import FindElement
import time

class ActionMethod():
    def __init__(self):
        pass

    #打开浏览器
    def open_browser(self,browser):
        if browser=='chrome':
            self.driver=webdriver.Chrome()
        elif browser=='edge':
            self.driver=webdriver.Edge()
        else:
            self.driver=webdriver.Firefox()

    #输入url地址
    def get_url(self,url):
        self.driver.get(url)

    #定位元素
    def get_element2(self,key):
        find_element=FindElement(self.driver)
        element=find_element.get_element1(key)
        return element

    #获取不到元素用于确认是否登录成功
    def is_element_in(self,key):
        element=self.get_element2(key)
        if element==None:
            return True


    #输入元素
    def send_value(self,key,value):
        element=self.get_element2(key)
        element.send_keys(value)

    #点击元素
    def click_element(self,key):
        element=self.get_element2(key)
        element.click()

    #等待
    def time_sleep(self,value):
        time.sleep(int(value))

    #获取title
    def get_title(self):
        return self.driver.title


    #关闭浏览器
    def close_browser(self):
        self.driver.close()