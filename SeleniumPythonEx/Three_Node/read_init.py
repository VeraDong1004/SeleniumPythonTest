#coding=utf-8
import configparser

class ReadIni:
    def __init__(self,load_path):
        '''构造函数'''
        self.data=self.load_ini(load_path)
    
    def load_ini(self,load_path):
        '''获取文件位置'''
        mes = configparser.ConfigParser()
        # 读取文件
        mes.read(load_path)
        #'E:\00-PycharmProjects\SeleniumPythonEx\config\LocalElement.ini'
        return mes

    def get_value(self,load_name,key):
        '''获取文件内容'''
        return self.data.get(load_name,key)

    def get_value1(self,key):
        '''获取同一local_name下的内容'''
        return self.data.get('user_element_join',key)

read_ini=ReadIni('E:\\00-PycharmProjects\\SeleniumPythonEx\\config\\LocalElement.ini')
#print(read_ini.get_value('user_element','signin'))
#print(cf.get_value('user_element','password'))

if __name__=='__main__':
    read_ini=ReadIni('E:\\00-PycharmProjects\\SeleniumPythonEx\\config\\LocalElement.ini')
    print(read_ini.get_value1('username'))







