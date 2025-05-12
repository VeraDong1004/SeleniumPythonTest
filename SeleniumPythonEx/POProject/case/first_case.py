#coding=utf-8
import os.path
import sys
import time
import HTMLTestRunner
from selenium import webdriver
sys.path.append('E:\\00-PycharmProjects\\SeleniumPythonEx\\POProject')
from business.login_business import LoginBusiness


class First_case():
    def __init__(self):
        driver=webdriver.Edge()
        driver.get('https://www.imooc.com/user/newlogin')
        driver.maximize_window()
        self.login_business=LoginBusiness(driver)

    def test_login_successful(self):
        self.login_business.login('username','password','login_btn','username_error','password_error','1301887182@qq.com','Vera@1125')
        time.sleep(3)
        if self.login_business.login_success('code_ele','login_btn')!=False:
            print('登录成功，case1执行成功！')

    def test_login_username_error(self):
        username_error=self.login_business.login('username','password','login_btn','username_error','password_error','1301887182','Vera@1125')
        time.sleep(3)
        if username_error==True:
            print('用户名错误，case2执行成功！')

    def test_login_password_error(self):
        password_error=self.login_business.login('username','password','login_btn','username_error','password_error','1301887182@qq.com','1234')
        time.sleep(3)
        if password_error==True:
            print('密码错误，case3执行成功！')


if __name__=='__main__':
    first_case=First_case()
    #first_case.test_login_username_error()
    #first_case.test_login_password_error()
    first_case.test_login_successful()




