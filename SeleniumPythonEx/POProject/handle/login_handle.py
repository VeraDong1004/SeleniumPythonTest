#coding=utf-8
from page.login_page import LoginPage


class LoginHandle():
    def __init__(self,driver):
        self.Login_p=LoginPage(driver)

    def send_username(self,key,username):
        '''输入用户名'''
        self.Login_p.get_username_element(key).send_keys(username)

    def send_password(self,key,password):
        '''输入密码'''
        self.Login_p.get_password_element(key).send_keys(password)

    def username_error_text(self,key):
        '''获取错误输入时显示的文字信息'''
        user_name_error=self.Login_p.get_username_error_element(key)
        if user_name_error!=None:
            user_name_text=user_name_error.get_attribute('textContent')
            return user_name_text

    def password_error_text(self,key):
        '''获取密码错误输入时显示的文字信息'''
        password_error=self.Login_p.get_password_error_element(key)
        if password_error!=None:
            password_error_text=password_error.get_attribute('textContent')
            return password_error_text

    def click_login_btn(self,key):
        '''点击登录按钮'''
        login_btn=self.Login_p.get_login_btn_element(key)
        if login_btn!=None:
            login_btn.click()

    def error_code_save(self,key):
        '''存在验证码时报错'''
        error_code=self.Login_p.get_error_code_element(key)
        if error_code!=None:
            return error_code



