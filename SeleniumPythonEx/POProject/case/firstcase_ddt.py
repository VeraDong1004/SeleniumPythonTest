#coding=utf-8

'''
用户名，密码，登录按钮，用户错误提示元素，密码错误提示元素，
用户名，密码
'''
import ddt
import unittest
import time
from selenium import webdriver
import os
import HTMLTestRunner
import sys
sys.path.append('E:\\00-PycharmProjects\\SeleniumPythonEx\\POProject')
from business.login_business import LoginBusiness
from util.excel_util import ExcelUtil

ex=ExcelUtil()
data=ex.get_data()

@ddt.ddt
class firstcaseDDT(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Edge()
        self.driver.get('https://imooc.com/user/newlogin')
        self.driver.maximize_window()
        self.loginbussness = LoginBusiness(self.driver)

    def tearDown(self):
        #用例失败时截图
        time.sleep(5)
        # 检查测试结果
        outcome = getattr(self, '_outcome', None)
        if outcome:
            # 获取所有错误和失败
            result = outcome.result
            errors = getattr(result, 'errors', []) + getattr(result, 'failures', [])
            # 如果有错误且driver可用
            if errors and hasattr(self, 'driver') and self.driver:
                # 创建报告目录
                # C:\Users\哈哈哈\PycharmProjects\Selenium练习合集\report
                report_dir = os.path.join(os.getcwd(), 'report')
                os.makedirs(report_dir, exist_ok=True)
                # 保存截图
                case_name = getattr(self, '_testMethodName', 'unknown_test')
                file_path = os.path.join(report_dir, f'{case_name}.png')
                try:
                    self.driver.save_screenshot(file_path)
                    print(f"Screenshot saved: {file_path}")
                except Exception as e:
                    print(f"Failed to save screenshot: {str(e)}")
        # 关闭driver
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

    @ddt.data(*data)
    def test_login(self,data):
        username_key, password_key, loginbtn_key, username_error_key, password_error_key, name, password=data
        self.loginbussness.login(username_key,password_key,loginbtn_key,username_error_key,password_error_key,name,password)
        time.sleep(5)
        success_info = self.loginbussness.login_success('code_ele', 'login_btn')
        self.assertIsNot(success_info, False, 'case failed!')

'''
    @ddt.data(
        [ 'username','password','login_btn','username_error','password_error',
             '1301887182@qq.com','Vera@1125'],

        ['username', 'password', 'login_btn', 'username_error', 'password_error',
         '1301887182', 'Vera@1125'],

        ['username', 'password', 'login_btn', 'username_error', 'password_error',
        '1301887182@qq.com', '1125'],

        ['username', 'password', 'login_btn', 'username_error', 'password_error',
        '1301887180@qq.com', 'Dong@1004'])

    @ddt.unpack
'''



if __name__=='__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(
        output='E:\\00-PycharmProjects\\SeleniumPythonEx\\report',  # 报告保存目录
        report_name='test_report',  # 报告名称
        report_title='report',  # 报告标题
        verbosity=2,
        combine_reports=True,  # 是否合并多个测试类的报告
        add_timestamp=True  # 为True时生成报告名字中含有时间戳
    ))