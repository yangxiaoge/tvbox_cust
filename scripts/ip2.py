# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import urllib.request
from json import load
import os
import re

# https://github.com/wineast/manuall-dns/blob/main/ip2.py
__author__ = 'Wineast'
# url = "http://cn.bing.com/search?q=ip&go=%E6%8F%90%E4%BA%A4&qs=n&form=QBLH&pq=ip&sc=8-2&sp=-1&sk=&cvid=14b93b305cdc4183875411c3d9edf938"

##  GET IP from Web ##

# url="http://city.ip138.com/ip2city.asp"
# url='http://ip.42.pl/raw'
# url = 'http://ip.42.pl/anything'
# url = "http://jsonip.com"


def ip1():
    url = "http://ip.42.pl/raw"
    ipAdd = urllib.request.urlopen(url).read()
    print("ip1 is " + ipAdd)
    return str(ipAdd, encoding = "utf8")


def ip2():
    url2 = "http://jsonip.com"
    ipAdd = load(urllib.request.urlopen(url2))['ip']
    print("ip2 is " + ipAdd)
    return ipAdd

def ip3():
    url = "http://myip.ipip.net/"
    html = urllib.request.urlopen(url).read()
    ipAdd = ''
    #当前 IP：123.456.78.90  来自于：中国 内蒙古 呼和浩特  电信
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    match = pattern.search(str(html, encoding = "utf8"))
    if match is not None:
        ipAdd = match[0]
    print("ip3 is " + ipAdd)
    return ipAdd

    # regex
    # print(str(html, encoding = "utf8"))
    # return str(html, encoding = "utf8")

processor_list = [ip1, ip2, ip3]
ipAddress = ''

for processor in processor_list:
    try:
        process_result = processor()
    except:
        # print("error on: " + processor.__name__)
        process_result = ''

    if process_result != '':
        # print("bingo:" + process_result)
        # print("print func: " + processor.__name__)
        ipAddress = process_result
        break
    else:
        print(processor.__name__ + " return empty, switch to next one")
if ipAddress != '':
    print("bingo, ip is " + ipAddress)
else:
    print("ip not found")
    os._exit(0)


# 创建文件夹
# if not os.path.exists('d:\pythonWork'):
#     os.mkdir('d:\pythonWork')

# file_object = open('d:\pythonWork\ip.txt')
# try:
#     preIp = file_object.read()
# finally:
#     file_object.close()
# if preIp == ipAddress:
#     os._exit(0)
# else:
#     file_object = open('d:\pythonWork\ip.txt', 'w+')
#     file_object.write(ipAddress)
#     file_object.close()


## Send to My email Address
# 第三方 SMTP 服务
key='xxxxxx'      #换成你的QQ邮箱SMTP的授权码(QQ邮箱设置里)
EMAIL_ADDRESS='xxxxx@qq.com'      #换成你的邮箱地址
EMAIL_PASSWORD=key

import smtplib
smtp=smtplib.SMTP('smtp.qq.com',25)

import ssl
context=ssl.create_default_context()
sender=EMAIL_ADDRESS    #发件邮箱
receiver=EMAIL_ADDRESS  #收件邮箱
from email.message import EmailMessage
subject='Manual_DNS_Service'
# body="Hello,this is an email sent by python!"
msg=EmailMessage()
msg['subject']=subject   #邮件主题
msg['From']=sender
msg['To']=receiver
msg.set_content('ip: ' + ipAddress)    #邮件内容

with smtplib.SMTP_SSL("smtp.qq.com",465,context=context) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
    print(u"邮件发送成功")