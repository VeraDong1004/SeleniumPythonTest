#coding=utf-8
from selenium.webdriver.common.by import By
from base.login_get_element import FindElement

class LoginPage():
    def __init__(self,driver):
        self.login_fd=FindElement(driver)

    def get_username_element(self,key):
        '''查找用户名元素'''
        username_ele=self.login_fd.get_element1(key)
        return username_ele

    def get_password_element(self,key):
        '''查找密码元素'''
        password_ele=self.login_fd.get_element1(key)
        return password_ele

    def get_username_error_element(self,key):
        '''查找用户名错误元素'''
        username_error_ele=self.login_fd.get_element1(key)
        return username_error_ele

    def get_password_error_element(self,key):
        '''查找密码错误元素'''
        password_error_ele=self.login_fd.get_element1(key)
        return password_error_ele


    def get_login_btn_element(self,key):
        '''查找登录按钮'''
        login_btn=self.login_fd.get_element1(key)
        if login_btn!=None:
            return login_btn

    def get_error_code_element(self,key):
        '''查找验证码'''
        error_code_element=self.login_fd.get_element1(key)
        if error_code_element!=None:
            return error_code_element




