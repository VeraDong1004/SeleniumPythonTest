#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
import time
import random
import sys
sys.path.append('E:\\00-PycharmProjects\\SeleniumPythonEx')
from Three_Node.read_init import read_ini

class Login():
    def __init__(self,browser='edge'):
        if browser=='edge':
            self.driver=webdriver.Edge()
        else:
            self.driver=webdriver.Firefox()
        time.sleep(2)

    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    def get_local_element(self, load_name, key):
        data = read_ini.get_value(load_name, key)
        data_info = data.split('>')
        return data_info

    def get_element(self, load_name, key):
        by,Value= self.get_local_element(load_name, key)
        if by == 'id':
            element = self.driver.find_element(By.ID, Value)
        elif by == 'name':
            element = self.driver.find_element(By.NAME, Value)
        elif by == 'class':
            element = self.driver.find_element(By.CLASS_NAME, Value)
        elif by == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, Value)
        else:
            element = self.driver.find_element(By.XPATH, Value)
        return element

    def user_name(self,i):
        user_name = ''.join(random.sample('1301887182', i)) + '@qq.com'
        return user_name

    def error_code(self,load_name,key,file_name):
        error_element=self.get_element(load_name,key)
        if error_element!=None:
            self.driver.get_screenshot_as_file(file_name)
        else:
            return None


    def als_pic(self,file_name):
        code = self.driver.find_element(By.XPATH,'//*[@id="signup-form"]/div[3]/a[1]/img')
        left =code.location['x']
        top = code.location['y']
        right = left + code.size['width']
        down = top + code.size['height']
        im = Image.open('e:\\error_pic.png')
        img = im.crop((left, top, right, down))
        img.save(file_name)
        image=Image.open(file_name)
        text=pytesseract.image_to_string(image)
        return text
        

    def main(self):
        user_name_btn=self.get_element('user_element_join','username')
        user_name_btn.send_keys(self.user_name(8))
        pwd_btn=self.get_element('user_element_join','password')
        pwd_btn.send_keys('Aa111111')
        time.sleep(2)
        login_btn=self.get_element('user_element_join','signin')
        login_btn.click()
        time.sleep(5)
        self.error_code('user_element_join','error_info','e:\\error_pic.png')
        code1=self.als_pic('e:\\error_pic1.png')
        code_element=self.get_element('user_element_join','code_ele')
        code_element.send_keys(code1)

        im = Image.open('e:\\error_pic.png')
        img = im.crop((2075, 845, 2245, 927))
        img.save('e:\\error_pic1.png')
        code2= pytesseract.image_to_string(img)
        print(code2)
        code_element.send_keys(code2)

        time.sleep(10)
        self.close_browse()



    def close_browse(self):
    
        self.driver.close()


login=Login()
login.open_url('https://imooc.com/user/newlogin')
login.main()


'''
im = Image.open('e:\\error_pic.png')
img = im.crop((2075,853,2245,907))
img.save('e:\\error_pic1.png')
text=pytesseract.image_to_string(img)
print(text)
'''