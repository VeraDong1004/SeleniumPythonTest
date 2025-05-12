#coding=utf-8
import sys
import time
sys.path.append('/')
from Three_Node.read_init import ReadIni
from Three_Node.open_browser import SeleniumDriver


selenium_driver=SeleniumDriver('edge')
read_Ini=ReadIni('/config/LocalElement.ini')

data=read_Ini.get_value('user_element','username')
data_info=data.split('>')
#print(data_info)
By=data_info[0]
value=data_info[1]
#print(By,'->',value)

selenium_driver.get_url('https://www.imooc.com/user/newlogin')
selenium_driver.send_value(By,value,'test12345')
time.sleep(3)
selenium_driver.close_driver()
