import os
from datetime import datetime
import pytz
import requests
import json


shanghaiTz = pytz.timezone("Asia/Shanghai")
timeNow = datetime.now(shanghaiTz)
print("timeNow=" + str(timeNow))
# 时间
# 2023
year = timeNow.strftime("%Y") # 指令中间不加#号就自动补零
# 08
month = timeNow.strftime("%m") # 指令中间不加#号就自动补零
# 21
day = timeNow.strftime("%d") # 指令中间不加#号就自动补零
# 20230821
today = timeNow.strftime("%Y-%m-%d") # 指令中间不加#号就自动补零

# print("today=" + today)

weekday = timeNow.weekday()

if weekday == 5 or weekday == 6:
    print("今天是周末！")
    weekend = True
else:
    print("今天是工作日。")
    weekend = False

def updateHolidayFile():
    # 创建文件夹
    if not os.path.exists("holiday"):
        os.mkdir("holiday")

    def httpGetText(url):
        try:
            req = requests.get(url, verify=False)
            if req.status_code == 200:
                return req.text
        except Exception as e:
            print(f'httpGetText failed: %s' % (e))
    
    def targetYear(targetYear):
        print("搜索"+str(targetYear)+"年国务院文件")
        tempisOffDay = weekend
        # print("tempisOffDay1="+str(tempisOffDay))
        try:
            result = httpGetText('https://raw.githubusercontent.com/NateScarlet/holiday-cn/master/' + str(targetYear) + '.json')
            if result:
                # print("----" + result)
                # 将 JSON 字符串转换为 Python 字典
                data = json.loads(result)
                # print(data['year'])
                # 国务院文件中今天是否工作日
                for item in iter(data['days']):
                    if item['date'] == today:
                    # if item['date'] == '2023-01-01': #元旦当前
                    # if item['date'] == '2023-04-23': #五一补班
                        tempisOffDay = item['isOffDay']
                # print("tempisOffDay2="+str(tempisOffDay))
                return tempisOffDay
                # print(isHolidayList)
                # return len(isHolidayList) != 0
        except Exception as e:
            print(f'targetYear failed: %s' % (e))

    # 最近三年文件都检查一遍，只要有一个国务院文件中查到，说明是放假的
    isOffDay = targetYear(int(year)-1) or targetYear(year) or targetYear(int(year)+1)
    print("放假="+str(isOffDay))
    myJson = {}
    myJson['date']=today
    myJson['isOffDay']=isOffDay
    jsonText = json.dumps(myJson, ensure_ascii=False)
    print("jsonText=" + jsonText)
    fp = open("holiday/isHoliday.json", "w+", encoding='utf-8')     
    fp.write(jsonText)
    fp.close()


if __name__ == "__main__":
    # 判断今天是否工作日
    updateHolidayFile()
