import os
import re
import base64
import datetime
import requests


# 创建文件夹
if not os.path.exists("tvbox"):
    os.mkdir("tvbox")
# tvbox源（TV软件下载地址：https://github.com/FongMi/TV）

def httpGetText(url):
    try:
        req = requests.get(url, verify=False)
        if req.status_code == 200:
            return req.text
    except Exception as e:
        print(f'httpGetText failed: %s' % (e))


# 源3 FongMi config
result = httpGetText('https://raw.githubusercontent.com/FongMi/CatVodSpider/main/json/config.json')
if result:
    fp = open("tvbox/fongmi_config.json", "w+", encoding='utf-8')
    # print("----" + result)
    fp.write(result)
    fp.close()
 
# 源4 FongMi 18+
result = httpGetText('https://raw.githubusercontent.com/FongMi/CatVodSpider/main/json/adult.json')
if result:
    fp = open("tvbox/fongmi_adult.json", "w+", encoding='utf-8')
    # print("----" + result)
    fp.write(result)
    fp.close()
    
# 源5 唐三
result = httpGetText('https://gh.t4tv.hz.cz/newtang.bmp')
if result:
    result = re.findall('(?<=\*\*).*$', result)[0]
    # print(result)
    # Decode
    result = base64.b64decode(result).decode('utf-8')
    print(result)
    fp = open("tvbox/tangsan", "w+", encoding='utf-8')
    # print("----" + result)
    fp.write(result)
    fp.close()

# 黎歌：https://www.lige.fit/ua
result = httpGetText('https://api.lige.fit/getJson')
if result:
    fp = open("tvbox/黎歌多仓.json", "w+", encoding='utf-8')
    # print("----" + result)
    transfer2Yingshi = '{"urls":' + result + '}'
    fp.write(transfer2Yingshi)
    fp.close()

