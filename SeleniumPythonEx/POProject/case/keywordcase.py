#coding=utf-8

import sys
import time

sys.path.append('E:\\00-PycharmProjects\\SeleniumPythonEx\\POProject')
from util.excel_util import ExcelUtil
from keywords.actionMethod import ActionMethod

class KeywordCase():
    def __init__(self):
        self.action_method = ActionMethod()
        self.results=[]#存储所有测试结果

    def run_main(self):
        handle_excel=ExcelUtil('E:\\00-PycharmProjects\\SeleniumPythonEx\\config\\keywords.xls')
        #获取行数
        case_lines=handle_excel.get_lines()
        if case_lines!=None:
            for i in range(case_lines):
                #获取是否执行标识
                is_run=handle_excel.get_col_value(i,3)
                if is_run=='yes':
                    #获取操作元素的值
                    send_key=handle_excel.get_col_value(i,5)
                    #获取操作方法
                    method=handle_excel.get_col_value(i,6)
                    #获取元素输入数据
                    send_value=handle_excel.get_col_value(i,7)
                    #获取结果的操作方法和预期值
                    except_result_method=handle_excel.get_col_value(i,8)
                    except_result_value=handle_excel.get_col_value(i,9)
                    #执行相应的操作
                    self.run_method(method,send_key,send_value)
                    time.sleep(2)
                    #判断结果是否符合预期并回填实际结果；
                    if except_result_value!='':
                        result_list=self.get_except_result_value(except_result_value)
                        if result_list[0]=='text':
                            result_value=self.run_method(except_result_method)
                            if result_list[1] in result_value:
                                handle_excel.write_value(i,10,'pass')
                            else:
                                handle_excel.write_value(i,10,'fail')

                        elif result_list[0]=='element':
                            result_value=self.run_method(except_result_method,result_list[1])
                            if result_value!=None:
                                handle_excel.write_value(i,10,'pass')
                            else:
                                handle_excel.write_value(i,10,'fail')
                        else:
                            print('只有以上两种情况！')

                    else:
                            print('预期结果为空！')

    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')


    def run_method(self,method,send_key='',send_value=''):
        #获取操作方法的值
        #用户动态获取对象的属性/方法
        '''例：
        method=send_value
        method=ActionMethod.send_value(key,value)'''
        method_func=getattr(self.action_method,method)
        if send_value!='' and send_key!='':
            #如果输入数据有值，则同时获取输入数据和当前需操作元素的值
            result=method_func(send_key,send_value)
        elif send_value==''and send_key=='':
            result=method_func()
        elif send_value!='' and send_key=='':
            result=method_func(send_value)
            #如果输入数据为空，则只需要获取当前需操作元素的值
        else:
            result=method_func(send_key)
        return result


if __name__=='__main__':
    test=KeywordCase()
    test.run_main()