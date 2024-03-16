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
    print("今天是周末！(只看周六周日)")
    weekend = True
else:
    print("今天是工作日。(只看周六周日)")
    weekend = False

class Holiday:
    def __init__(self, contain, name, isHoliday, datee):
        self.contain = contain
        self.name = name
        self.isHoliday = isHoliday
        self.datee = datee

    def get_contain(self):
        return self.contain
    
    def get_name(self):
        return self.name
    
    def get_isHoliday(self):
        return self.isHoliday
    
    def get_date(self):
        return self.datee

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
        if weekend:
            tempName = "周末"
        else:
            tempName = "工作日"
        holidayBean = Holiday(False, tempName, weekend, today)
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
                        holidayBean.contain = True
                        holidayBean.name = item['name']
                        holidayBean.isHoliday = item['isOffDay']
                        holidayBean.datee = today
                # print("tempisOffDay2="+str(tempisOffDay))
                return holidayBean
                # print(isHolidayList)
                # return len(isHolidayList) != 0
        except Exception as e:
            print(f'targetYear failed: %s' % (e))
        
        return holidayBean


    myJson = {}
    # 最近三年文件都检查一遍，只要有一个国务院文件中查到，说明是有法定假日安排（放假后者补班，即使今天本来是周末也只能参考法定假日安排！）
    lastYear = targetYear(int(year)-1)
    thisYear = targetYear(year)
    nextYear = targetYear(int(year)+1)
    if lastYear.contain or thisYear.contain or nextYear.contain:
        if lastYear.contain:
            isOffDay = lastYear.isHoliday
            myJson['name'] = lastYear.name
            if isOffDay:
                myJson['desc'] = "放假"
            else:
                myJson['desc'] = "法定补班"
        if thisYear.contain:
            isOffDay = thisYear.isHoliday
            myJson['name'] = thisYear.name
            if isOffDay:
                myJson['desc'] = "放假"
            else:
                myJson['desc'] = "法定补班"
        if nextYear.contain:
            isOffDay = nextYear.isHoliday   
            myJson['name'] = nextYear.name
            if isOffDay:
                myJson['desc'] = "放假"
            else:
                myJson['desc'] = "法定补班"
    else:
        isOffDay = weekend
        if weekend:
            tempName = "周末"
        else:
            tempName = "工作日"
            
        myJson['name'] = tempName
        
        if isOffDay:
            myJson['desc'] = "放假"
        else:
            myJson['desc'] = "搬砖"
    
    if isOffDay:
        print("今日放假")   
    else:
        print("今日搬砖") 
        
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
