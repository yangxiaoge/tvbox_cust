# coding:utf-8
import urllib.request
from json import load
import os
import re
import argparse
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

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


def getIp():
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
        result = sendEmail("ip地址", ipAddress)
        if result:
            print("发送成功！")
        else:
             print("发送失败！")
    else:
        print("ip not found")
        os._exit(0)
    

# 发送邮件消息
def sendEmail(title, errorMsg):
    ret=True
    try:
        msg=MIMEText(errorMsg,'plain','utf-8')
        msg['From']=formataddr(["GithubAction",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["Bruce",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=title                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("sendEmail failed: " +str(e))
        ret=False
    return ret


# 全局变量
my_sender=''    # 发件人邮箱账号
my_pass = ''    # 发件人邮箱密码
my_user=''      # 收件人邮箱账号，我这边发送给自己
telegram_bot_token=''  #telegram_bot_token
telegram_bot_id='' #telegram_bot_id

if __name__ == "__main__":
    # 读取github环境变量值
    parser = argparse.ArgumentParser(description='读取secrets')
    parser.add_argument('--telegram_bot_token', type=str, help='telegram_bot_token')
    parser.add_argument('--telegram_bot_id', type=str, help='telegram_bot_id')
    parser.add_argument('--email_sender', type=str, help='email_sender')
    parser.add_argument('--email_pass', type=str, help='email_pass')
    parser.add_argument('--email_receive', type=str, help='email_receive')
    args = parser.parse_args()

    # 赋值
    my_sender=args.email_sender
    my_pass=args.email_pass
    my_user=args.email_receive
    telegram_bot_token=args.telegram_bot_token
    telegram_bot_id=args.telegram_bot_id
    
    getIp()
