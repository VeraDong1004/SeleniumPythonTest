#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
edge_options=EdgeOptions()
#默认下载路径,禁止弹出下载窗口
prefs={'download.default_directory':'e:\\','profile.default_content_settings.popups':0}
edge_options.add_experimental_option('prefs',prefs)

driver=webdriver.Edge(options=edge_options)
driver.get('https://www.imooc.com/mobile/app')
#关闭弹窗
driver.find_element(By.ID,'js-advpop-close').click()
time.sleep(2)
#点击下载
driver.find_element(By.CLASS_NAME,'imv2-android').click()
time.sleep(5)
driver.close()