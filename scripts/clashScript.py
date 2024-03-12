import os
import re
import datetime
import requests
import argparse
import base64
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 时间
year = datetime.datetime.today().strftime("%Y") # 指令中间不加#号就自动补零
month = datetime.datetime.today().strftime("%m") # 指令中间不加#号就自动补零
day = datetime.datetime.today().strftime("%d") # 指令中间不加#号就自动补零
date = datetime.datetime.today().strftime("%Y%m%d") # 指令中间不加#号就自动补零

def download_clash():
    # 创建文件夹
    if not os.path.exists("clash"):
        os.mkdir("clash")

    def httpGetText(url):
        try:
            req = requests.get(url, verify=False)
            if req.status_code == 200:
                return req.text
        except Exception as e:
            print(f'httpGetText failed: %s' % (e))

    # 免费节点
    result = httpGetText('https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml')
    if result:
        fp = open("clash/Clash.yml", "w+", encoding='utf-8')
        # print("----" + result)
        fp.write(result)
        fp.close()
        
    # 免费节点1
    result = httpGetText('https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml')
    if result:
        fp = open("clash/Clash1.yml", "w+", encoding='utf-8')
        # print("----" + result)
        fp.write(result)
        fp.close()

    # 免费节点2
    result = httpGetText('https://raw.githubusercontent.com/ripaojiedian/freenode/main/clash')
    if result:
        fp = open("clash/Clash2.yml", "w+", encoding='utf-8')
        # print("----" + result)
        fp.write(result)
        fp.close()

    #https://clashnode.com/wp-content/uploads/2023/04/20230419.yaml
    # 免费节点3
    result = httpGetText("https://clashnode.com/wp-content/uploads/" + year + "/" + month + "/" + date + ".yaml")
    if result:
        fp = open("clash/Clash3.yml", "w+", encoding='utf-8')
        # print("----" + result)
        fp.write(result)
        fp.close()
        
    # 免费节点4
    result = httpGetText("https://raw.githubusercontent.com/vxiaov/free_proxy_ss/main/clash/clash.provider.yaml")
    if result:
        fp = open("clash/Clash4.yml", "w+", encoding='utf-8')
        # print("----" + result)
        fp.write(result)
        fp.close()

    # 免费节点5
    result = httpGetText('https://raw.githubusercontent.com/aiboboxx/clashfree/main/clash.yml')
    if result:
        fp = open("clash/Clash5.yml", "w+", encoding='utf-8')
        # print("----" + result)
        fp.write(result)
        fp.close()

    # 免费节点6
    result = httpGetText('https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub')
    if result:
        fp = open("clash/Clash6.yml", "w+", encoding='utf-8')
        # print("----" + result)
        fp.write(result)
        fp.close()
        
    # 免费节点7
    result = httpGetText('https://raw.githubusercontent.com/Flik6/getNode/main/clash.yaml')
    if result:
        fp = open("clash/Clash7.yml", "w+", encoding='utf-8')
        # print("----" + result)
        fp.write(result)
        fp.close()

        

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
        print(str(e))
        ret=False
    return ret


# 给telegram机器人发送消息
def sendTelegramBot(errorMsg):
    ret=True
    try:
        r = requests.post(f'https://api.telegram.org/bot' + telegram_bot_token + '/sendMessage', json={"chat_id": telegram_bot_id, "text": errorMsg})
        if r.status_code == 200:
            ret=True
        else:
            ret=False
        return ret
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(str(e))
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

    # 下载文件
    download_clash()
