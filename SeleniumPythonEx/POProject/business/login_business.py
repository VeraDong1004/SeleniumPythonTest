#coding=utf-8
from handle.login_handle import LoginHandle

class LoginBusiness():
    def __init__(self,driver):
        self.login_handle=LoginHandle(driver)
    #执行操作
    def login(self,username_key,password_key,loginbtn_key,username_error_key,password_error_key,name,password):
        self.login_handle.send_username(username_key,name)
        self.login_handle.send_password( password_key, password)
        self.login_handle.click_login_btn( loginbtn_key)

        username_error_text=self.login_handle.username_error_text(username_error_key)
        if username_error_text=='请输入正确的邮箱或手机号':
            return True
        '''
        else:
            print('用户名校验成功！')
        '''

        password_error_text = self.login_handle.password_error_text(password_error_key)
        if password_error_text == '请输入6-20位密码，区分大小写，不能使用空格！':
            return True
        '''
        else:
            print('密码校验成功！')
        '''

    def login_success(self,key,login_key):
        login_success_btn=self.login_handle.error_code_save(key)
        login_success_btn1=self.login_handle.Login_p.get_login_btn_element(login_key)
        if login_success_btn!=None or login_success_btn1!=None:
            return False



