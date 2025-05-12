#coding=utf-8
import logging
import os
import datetime

class UserLog:
    def __init__(self):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
#控制台输出日志
#consle=logging.StreamHandler()
#logger.addHandler(consle)
#logger.debug('1536474')
#consle.close()
#logger.removeHandler(consle)

#文件名
#C:\Users\哈哈哈\PycharmProjects\Selenium练习合集\PO模型设计\log
        base_path=os.path.dirname(os.path.abspath(__file__))
        #C:\Users\哈哈哈\PycharmProjects\Selenium练习合集\PO模型设计\log]\logs
        log_path=os.path.join(base_path,'logs')
        log_file=datetime.datetime.now().strftime('%y-%m-%d')+'.log'
        log_name=log_path+'\\'+log_file

        #文件输出日志
        self.file_handle=logging.FileHandler(log_name,'a',encoding='utf-8')
        #设置等级
        self.file_handle.setLevel(logging.INFO)
        #修改文件格式
        formatter=logging.Formatter('%(asctime)s %(filename)s --> %(funcName)s %(levelno)s %(levelname)s --> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        #self.logger.debug('vera')


    def get_log(self):
        return self.logger


    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__=='__main__':
    user=UserLog()
    log=user.get_log()
    log.debug('this is a tample')
    user.close_handle()
