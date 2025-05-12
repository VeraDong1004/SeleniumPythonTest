#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time
import pytesseract
'''
driver=webdriver.Edge()
driver.get('https://www.imooc.com')
driver.maximize_window()
time.sleep(2)
#获取全面截图
driver.save_screenshot('E:\\imooc.png')
#获取图片大小
element=driver.find_elements(By.CLASS_NAME,'system-class-icon')[0]
left=element.location['x']
top=element.location['y']
right=left+element.size['width']
down=top+element.size['height']
print(left,right,top,down)
#裁剪照片并重新保存

im=Image.open('E:\\imooc.png')
img=im.crop((left,top,right,down))
img.save('E:\\imooc1.png')
'''
#从图片中读取文字
image=Image.open('E:\\imooc2test.png')
text=pytesseract.image_to_string(image)
print(text)

#driver.close()