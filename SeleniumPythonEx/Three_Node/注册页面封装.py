#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from PIL import Image
import pytesseract

driver = webdriver.Edge()
def open_browser():
    driver.get('https://www.imooc.com/user/newlogin')
    driver.maximize_window()
    time.sleep(2)

def get_element(style,key):
    '''获取元素'''
    if style=='id':
        element=driver.find_element(By.ID,key)
    elif style=='name':
        element=driver.find_element(By.NAME,key)
    elif style=='class':
        element = driver.find_element(By.CLASS_NAME,key)
    elif style=='css':
        element=driver.find_element(By.CSS_SELECROT,key)
    else:
        element=driver.find_element(By.XPATH,key)
    return element

def user_info(str_list,num):
    '''随机生成用户名称和用户密码'''
    user_name=''.join(random.sample(str_list,num))
    return user_name


def ans_pic(file_name):
    '''从图片中读取文字'''
    driver.save_screenshot(file_name)
    element = driver.find_elements(By.CLASS_NAME, 'rlf-autoin')[0]
    left = element.location['x']
    top = element.location['y']
    right = left + element.size['width']
    down = top + element.size['height']
    # 裁剪照片并重新保存
    im = Image.open(file_name)
    img = im.crop((left, top, right, down))
    img.save(file_name)
    image=Image.open(file_name)
    text=pytesseract.image_to_string(image)
    return text


open_browser()
#输入用户名
user_name=user_info('123456abcdef',8)
get_element('name','email').send_keys(user_name)
#获取密码
pwd=ans_pic('E:\\test.png')
#输入密码
get_element('name','password').send_keys(pwd)
#点击注册按钮
driver.find_elements(By.CLASS_NAME,'rlf-group')[4].click()
#关闭浏览器
time.sleep(5)
driver.close()






