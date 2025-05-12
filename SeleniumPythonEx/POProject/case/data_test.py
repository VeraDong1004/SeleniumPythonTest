#coding=utf-8
import ddt
import unittest
@ddt.ddt
class Datatest(unittest.TestCase):
    def setUp(self):
        print('这是前置条件')

    def tearDown(self):
        print('这是后置条件')


    @ddt.data(
        ['1','2'],
        [3,4],
        [5,6]
    )

    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)

if __name__=='__main__':
    unittest.main()