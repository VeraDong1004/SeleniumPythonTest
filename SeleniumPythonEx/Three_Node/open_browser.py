#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import sys
from Three_Node.handle_cookie import cookie
sys.path.append('E:\\00-PycharmProjects\\SeleniumPythonEx')
from Three_Node.read_init import read_ini
from selenium.webdriver.support.select import Select
from pykeyboard import PyKeyboard
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Three_Node.handle_json import handle_json


'''
#打开浏览器
driver=webdriver.Edge()
#等待5s
time.sleep(5)
#查询指定网页
driver.get('https://www.baidu.com')
#等待5s
time.sleep(5)
#关闭浏览器
driver.close()
'''

'''
def open_browser(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='edge':
        driver=webdriver.Edge()
    elif browser=='ie':
        driver=webdriver.Ie()
#open_browser('edge')
'''
class SeleniumDriver:
    def __init__(self,browser):
        '''打开浏览器'''
        self.browser=browser
        if self.browser=='firefox':
            self.driver=webdriver.Firefox()
        elif self.browser=='edge':
            edge_options = EdgeOptions()
            # 默认下载路径,禁止弹出下载窗口
            prefs = {'download.default_directory': 'e:\\', 'profile.default_content_settings.popups': 0}
            edge_options.add_experimental_option('prefs', prefs)
            self.driver=webdriver.Edge(options=edge_options)
        else:
            print('仅支持Firefox/Edge,暂不支持其他浏览器！！！')
        time.sleep(2)

    def get_url(self,url):
        '''打开对应的URL'''
        if self.driver!=None:
            self.driver.maximize_window()
            time.sleep(3)
            if 'https://' in url:
                self.driver.get(url)
            else:
                print('URL输入有误，请重新输入！')
            time.sleep(2)

    def assert_title(self, title_name=None):
        '''
        判断title是否正确
        '''
        if title_name != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def open_url_is_true(self,url, title_name=None):
        '''判断打开的网页对应的title是否正确'''
        self.get_url(url)
        return self.assert_title(title_name)

    def switch_window(self,title_name):
        '''通过title切换窗口'''
        handle_lists=self.driver.window_handles
        current_handle=self.driver.current_window_handle
        for i in handle_lists:
            if i.title!=current_handle:
                time.sleep(2)
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'qr-change-logo').click()
        time.sleep(2)

    def get_element(self,name,key):
        '''获取元素'''
        element=None
        BY,Value=self.get_local_element(name,key)
        try:
            if BY=='id':
                element=self.driver.find_element(By.ID,Value)
            elif BY=='name':
                element=self.driver.find_element(By.NAME,Value)
            elif BY=='class':
                element=self.driver.find_element(By.CLASS_NAME,Value)
            elif BY=='css':
                element=self.driver.find_element(By.CSS_SELECTOR,Value)
            else:
                element=self.driver.find_element(By.XPATH,Value)
        except:
            print('定位方式：',BY,'定位值：',Value,'定位元素失败，请检查并重新输入！')
        return self.element_is_display(element)

    def get_elements(self,name,key):
        by,value=self.get_local_element(name,key)
        if by == 'id':
            elements = self.driver.find_elements(By.ID, value)
        elif by == 'name':
            elements = self.driver.find_elements(By.NAME, value)
        elif by == 'class':
            elements = self.driver.find_elements(By.CLASS_NAME, value)
        elif by == 'css':
            elements = self.driver.find_elements(By.CSS_SELECTOR, value)
        else:
            elements = self.driver.find_elements(By.XPATH, value)
        return elements

    def get_level_element(self,level_name,level_key,node_name,node_key):
        '''按照层级查找元素'''
        element=self.get_element(level_name,level_key)
        node_by,node_value=self.get_local_element(node_name,node_key)
        if element==False:
            return element
        if node_by=='id':
            element1=element.find_element(By.ID,node_value)
        elif node_by=='name':
            element1=element.find_element(By.NAME,node_value)
        elif node_by=='class':
            element1=element.find_element(By.CLASS_NAME,node_value)
        elif node_by=='css':
            element1=element.find_element(By.CSS_SELECTOR,node_value)
        else:
            element1=element.find_element(By.XPATH,node_value)
        return self.element_is_display(element1)


    def get_list_element(self,name,key,index):
        '''通过list封装查找元素'''
        elements=self.get_elements(name,key)
        if elements==False:
            return elements
        if index>len(elements):
            return None
        return elements[index]

    def send_value(self,name,key,values):
        '''输入封装'''
        element=self.get_element(name,key)
        if element==False:
            print('输入失败，定位元素不可编辑！')
        else:
            if element!=None:
                element.send_keys(values)
            else:
                print('输入失败，定位元素没找到！')

    def click_element(self,name,key):
        '''点击封装'''
        element=self.get_element(name,key)
        if element==False:
            print('点击失败,定位元素不可见！')
        else:
            if element!=None:
                element.click()
            else:
                print('点击失败，元素没找到！')


    def checkbox_is_selected(self,name,key,value=None):
        '''检查checkbox是否被选中'''
        element=self.get_element(name,key)
        if element !=False:
            flag=element.is_selected()
            if flag==True:
                if value!='check':
                    self.click_element(name,key)
            else:
                if value=='check':
                    self.click_element(name,key)
        else:
            print('元素不可见，没办法选中！')

    def element_is_display(self,element):
        '''检查页面元素是否正常显示'''
        flag=element.is_displayed()
        if flag==True:
            return element
        else:
            print('元素未显示！')

    def get_local_element(self,name,key):
        '''通过读取文件中的值定位元素'''
        data = read_ini.get_value(name,key)
        data_info = data.split('>')
        return data_info

    def get_select(self,name,key,value,index=None):
        '''通过index获取selected-下拉框数据'''
        select_element=None
        if index!=None:
            select_element=self.get_list_element(name,key,index)
        else:
            select_element=self.get_element(name,key)
        return Select(select_element).select_by_value(value)

    def upload_file(self,file_name):
        pykey = PyKeyboard()
        '''
        非input类型上传文件
        # 切换输入法
        pykey.tap_key(pykey.shift_key)
        '''
        pykey.type_string(file_name)
        time.sleep(2)
        pykey.tap_key(pykey.enter_key)

    def download_file(self,by,name):
        '''下载文件'''
        self.click_element(by,name)

    def js_excute_calender(self,name,key):
        '''执行js属性'''
        local=self.get_local_element(name,key)
        by=local[0]
        value=local[1]
        if by=='id':
            by_key='getElementById'
            js='document.%s("%s").removeAttribute("readonly");'%(by_key,value)
        else:
            by_key='getElementByClassName'
            js='document.%s("%s")[1].removeAttribute("readonly");'%(by_key,value)
        self.driver.excute_script(js)

    def calendar(self,name,key,value):
        '''修改日历'''
        element=self.get_element(name,key)
        try:
            element.get_attribute('readonly')
            self.js_excute_calender(name,key)
        except:
            print('这个不是只读属性的日历！')
        element.clear()
        self.send_value(name,key,value)

    def moveto_element_mouse(self,name,key):
        '''移动鼠标显示页面'''
        element=self.get_element(name,key)
        ActionChains(self.driver).move_to_element(element).perform()

    def refresh_F5(self):
        '''ctrl+F5刷新页面:强制刷新'''
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).perform()
        time.sleep(2)
        ActionChains(self.driver).key_up(Keys.CONTROL).perform()

    def switch_frame(self,name=None,key=None):
        '''富文本的输入:切换iframe'''
        if name!=None and key!=None:
            iframe_element=self.get_element(name,key)
            self.driver.switch_to(iframe_element)
        else:
            self.driver.switch_to.deafult_content()


    def switch_alert(self,info,value=None):
        '''系统级弹窗
        @parame info:确认or取消
        @parame value:是否需要输入的值'''
        windows_alert=self.driver.switch_to.alert
        if info=='accept':
            if value==None:
                windows_alert.accept()
            else:
                windows_alert.send_keys(value)
                windows_alert.accept()
        else:
            windows_alert.dismiss()

    def scroll_get_element(self,list_name,list_key,str_info):
        '''滑动查找元素
        list_name:元素列表查找方式；
        list_key:元素列表查找关键字
        str_info:最终查找元素包含的文本信息'''
        T=True
        js='document.documentElement.scrollTop=100;'
        list_element=self.get_elements(list_name,list_key)
        while T:
            for element in list_element:
                title_name=element.find_element(By.TAG_NAME,'a').text
                if title_name in str_info:
                    element.click()
                    T=False
            self.driver.execute_script(js)
            time.sleep(3)

    def scroll_element(self,name,key):
        '''滑动查找元素'''
        js = 'document.documentElement.scrollTop=100;'
        t=True
        while t:
            try:
                self.get_element(name,key)
                t=False
            except:
                self.driver.execute_script(js)

    def get_cookie(self):
        #接口
        #依赖
        cookie=self.driver.get_cookies()
        handle_json.write_data(cookie)

    def set_cookis(self):
        '''植入cookie'''
        cookie=handle_json.get_data()
        self.driver.delete_all_cookies()
        time.sleep(1)
        self.driver.add_cookie(cookie)
        time.sleep(2)

    def save_png(self):
        now_time=time.strftime('%Y%m%d.%H.%M.%S')
        self.driver.get_screenshot_as_file('%s.png' %now_time)



    def close_driver(self):
        '''关闭浏览器'''
        self.driver.close()






selenium_driver=SeleniumDriver('edge')
selenium_driver.get_url('https://www.imooc.com')
time.sleep(2)
selenium_driver.click_element('close_window','win_close')
time.sleep(2)
selenium_driver.get_url('https://www.imooc.com/wenda')
selenium_driver.scroll_get_element('scroll_test_element','list_elements','我现在的情况能找到工作吗？')
time.sleep(3)
selenium_driver.save_png()
time.sleep(2)
selenium_driver.close_driver()





