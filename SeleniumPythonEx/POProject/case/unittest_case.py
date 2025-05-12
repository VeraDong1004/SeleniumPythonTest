#coding=utf-8
import time
import unittest
from selenium import webdriver
import os
import HTMLTestRunner
import sys
sys.path.append('E:\\00-PycharmProjects\\SeleniumPythonEx\\POProject')
from business.login_business import LoginBusiness

from log.user_log import UserLog




class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver=webdriver.Edge()
        self.driver.get('https://imooc.com/user/newlogin')
        self.logger.info('this is test tmple')
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

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    #@unittest.skip('skip case1')
    def testcase01_login_successful(self):

        self.loginbussness.login('username','password',
                                  'login_btn','username_error',
                                  'password_error', '1301887182@qq.com', 'Vera@1125')
        time.sleep(5)
        success_info=self.loginbussness.login_success('code_ele','login_btn')
        #if success_info == True:
         #   print('登录成功，case1执行成功！')
        #通过assert判断用例是否执行成功
        self.assertIsNot(success_info,False,'case1 failed!')

    #@unittest.skip('skip case2')
    def testcase02_username_error(self):
        username_error = self.loginbussness.login('username','password',
                                                   'login_btn',
                                                   'username_error',  'password_error',
                                                   '1301887182', 'Vera@1125')
        time.sleep(3)
        #if username_error == True:
         #   print('用户名错误，case2执行成功！')
        self.assertTrue(username_error)

    #@unittest.skip('skip case3')
    def testcase03_password_error(self):
        password_error = self.loginbussness.login( 'username', 'password',
                                                   'login_btn',
                                                   'username_error', 'password_error',
                                                   '1301887182@qq.com', '1234')
        time.sleep(3)
        #if password_error == True:
         #   print('密码错误，case3执行成功！')
        self.assertTrue(password_error)

    '''
    @classmethod
    def setUpClass(cls):
        print('这是所有case的前置条件')

    @classmethod
    def tearDownClass(cls):
        print('这是所有case的后置条件')

    def setUp(self):
        print('这个是case的前置条件')

    def tearDown(self):
        print('这个是case的后置条件')

    def testfirstcase01(self):
        print('这是第一个case')

    def testsecondcase02(self):
        print('这是第二个case')
        
'''


if __name__ == '__main__':
    #使用HTMLTestRunner运行测试
    report_dir='E:\\00-PycharmProjects\\SeleniumPythonEx\\report'
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(
            output=report_dir,  # 报告保存目录
            report_name='test_report',  # 报告名称
            report_title='report', # 报告标题
            verbosity=2,
            combine_reports=True,  # 是否合并多个测试类的报告
            add_timestamp=True  #为True时生成报告名字中含有时间戳
    ))
    '''使用装饰器选择需要运行的case
    suite=unittest.TestSuite()
    suite.addTest(FirstCase01('testfirstcase01'))
    unittest.TextTestRunner().run(suite)
    '''




