#coding=utf-8
import unittest

class FirstCase02(unittest.TestCase):

    def setUp(self):
        print('这是case的前置条件！')

    def tearDown(self):
        print('这是case的后置条件！')

    @classmethod
    def setUpClass(cls):
        print('这是所有case的前置条件！')

    @classmethod
    def tearDownClass(cls):
        print('这是所有case的后置条件！')

    def testcase001(self):
        print('这是第一条case!')

    def testcase002(self):
        print('这是第二条case!')

    @unittest.skip('跳过第三条case!')
    def testcase003(self):
        print('这是第三条case!')

    def testcase004(self):
        print('这是第四条case!')

if __name__=='__main__':
    '''
    执行所有case
    unittest.main()
    '''
    #执行选中的case
    suite=unittest.TestSuite()
    suite.addTest(FirstCase02('testcase002'))
    suite.addTest(FirstCase02('testcase004'))
    suite.addTest(FirstCase02('testcase003'))
    suite.addTest(FirstCase02('testcase001'))
    unittest.TextTestRunner().run(suite)