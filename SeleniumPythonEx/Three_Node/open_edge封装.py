#coding=utf-8
from selenium import webdriver
import time
#类使用
class SeleniumDriver:
    def __init__(self, browser):
        self.browser = browser
        if self.browser=='chrome':
            self.driver=webdriver.Chrome()
        elif self.browser=='firefox':
            self.driver=webdriver.Firefox()
        elif self.browser=='ie':
            self.driver=webdriver.Ie()
        else:
            self.driver=webdriver.Edge()
        time.sleep(5)

    ####################################################
    #封装打开浏览器的方法
    def get_url(self, url):
        if self.driver != None:
            self.driver.maximize_window()
            if 'https://' in url:
                self.driver.get(url)
                time.sleep(3)
            else:
                print('你的URL输入有问题！')
        else:
            print('case失败！')

    def handle_windows(self, *args):
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'refresh':
                self.driver.refresh()
            elif args[0] == 'forward':
                self.driver.forward()
            else:
                print('传递参数有误，请重新输入！')
        elif value == 2:
            self.driver.set_window_size(args[0], args[1])
        else:
            print('传递参数有误，请重新输入！')
        time.sleep(5)


#打开地址的二次开发
#driver=open_browser('edge')
#get_url('http://www.imooc.com')
#error_study()
#handle_windows('max')

selenium_driver = SeleniumDriver('edge')
selenium_driver.handle_windows('max')
selenium_driver.get_url('https://www.baidu.com')
