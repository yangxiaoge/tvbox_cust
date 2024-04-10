# -*- coding: utf-8 -*-
# @Time : 2024/04/10 13:51
# @Author : Bruce
# @File : 
# @Software : PyCharm
# @Description : Selenium批量废弃代办任务（慎用）

# 能不能让我的程序连接到浏览器.让浏览器来完成各种复杂的操作，我们只接受最终的结果
# Selenium：自动化测试工具
# 可以:打开浏览器.然后像人一样去操作浏览器
# 程序员可以从Selenium中直接提取网页上的各种信息
import time

from selenium.webdriver import Edge
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 云之家账号
account='xxxxxxx'
# 云之家密码
pwd='xxxxx'
# 员工姓名
userName='xxx'

# 创建Edge浏览器对象
# web = Edge()
web = Chrome()
# 打开拉钩
web.get("https://www.yunzhijia.com/home/?m=open&a=login&utm_source=&utm_medium=")

print(web.title)
print("-------------------")
print(web)

# 账号输入模式
web.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div/div/h3/div[2]').click()
time.sleep(3)  # 让浏览器缓一会

# 搜索框输入"手机号"
input = web.find_element(By.XPATH,'//*[@id="email"]')
input.send_keys(account, Keys.NULL)
time.sleep(1)  # 让浏览器缓一会

# 搜索框输入"密码"
input = web.find_element(By.XPATH,'//*[@id="password"]')
input.send_keys(pwd, Keys.NULL)
time.sleep(1)  # 让浏览器缓一会

# 登录按钮
web.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div/div/div[1]/form/div[2]/input[3]').click()
time.sleep(3)  # 让浏览器缓一会

cookie_list=web.get_cookies()
print("cookie=" + str(cookie_list))

# 关闭网页
web.close()
print('网页结束！')
