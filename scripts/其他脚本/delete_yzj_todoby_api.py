# -*- coding: utf-8 -*-
# @Time : 2024/04/10 13:51
# @Author : Bruce
# @File : 
# @Software : PyCharm
# @Description : 批量废弃代办任务（慎用）

import requests
import json
from concurrent.futures import ThreadPoolExecutor

# 登录后的cookie
cookie = 'logintype5b45a7bae4b0254557bxxxxxxxxx'
# 用户凭证
ticket = 'APPURLWITHTI161xxxxxxxxxx'


def httpGetText(url):
    try:
        req = requests.get(url, verify=False)
        if req.status_code == 200:
            return req.text
    except Exception as e:
        print(f'httpGetText failed: %s' % (e))


def abandonTask(taskId):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        'Cookie': cookie
    }
    body = {"taskId": str(taskId), "opMsg": "", "language": "zh-CN"}
    req2 = requests.post("https://www.yunzhijia.com/workflow/api/v1/flow/abandonFlow?appId=10104" +
                         "&ticket="+ticket, data=body, headers=headers, verify=False)
    print("----" + req2.text)


def main():
    # 添加请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        'Cookie': cookie
    }
    result = httpGetText(
        "https://www.yunzhijia.com/workflow/api/v1/flowWeb/todoPageList?appId=10104"+"&ticket="+ticket)
    taskIds = []
    if result:
        print("----所有代办任务----\n" + result)
        # 将 JSON 字符串转换为 Python 字典
        data = json.loads(result)
        for item in iter(data['data']['content']):
            if item['noApproveType'] == 'NEED_TO_EDIT':
                taskIds.append(item['taskId'])
    print("taskIds="+str(taskIds))
    if len(taskIds) != 0:
        # 线程删除
        for taskId in taskIds:
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.submit(abandonTask, taskId)
        main()
    else:
        print("任务结束！")


if __name__ == '__main__':
    main()
