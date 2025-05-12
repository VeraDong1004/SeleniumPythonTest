#coding=utf-8
import unittest
import os

class RunCase(unittest.TestCase):
    def test_runcase01(self):
        case_path=os.path.join(os.getcwd(),'E:\\00-PycharmProjects\\SeleniumPythonEx\\POProject\\case')
        suite01=unittest.defaultTestLoader.discover(case_path,'unittest_c*.py')
        unittest.TextTestRunner().run(suite01)

if __name__=='__main__':
    unittest.main()