#!/bin/bash
#############版权信息#################
# 本脚本作者：bruce
# 版本：V1.0
# 日期：2024年03月16日
#############版权信息#################
#############pushplus信息#############
#文本的标题
title="${1}"                                             #①推送文本的标题可以自定义
#pushplus的token
token="${2}"                                             #②改成自己的pushplus的token(读取github入参)
# 群组编码
topic="${3}"                                             #③改成自己pushplus的群组编码(读取github入参)
#############pushplus信息#############

# 删除临时天气文件数据
rm -rf weather_data.json

#############天气信息#############
#城市
city="${4}"                                                  #④改成自己需要设置的城市(读取github入参)
#城市天气代码
city_code="${5}"                                             #⑤改成自己需要查询的和风天气的城市代码打开 https://c1.ywsj.link/s/m1Sv/doc?name=China-City-List-latest.xlsx 查询 (读取github入参)
#和风天气key
hefeng_key="${6}"                                            #⑥改成自己的和风天气的key (读取github入参)
# 发送HTTP请求并将JSON响应存储到临时文件中
curl -s -o weather_data.json "https://devapi.qweather.com/v7/weather/3d?location=${city_code}&key=${hefeng_key}" --compressed --header "Accept-Charset: UTF-8"
# 检查文件是否存在
if [ ! -f weather_data.json ]; then
    echo "无法获取天气数据。请检查weather_data.json是否存在"
    exit 1
fi

# 使用jq解析JSON数据
updateTime=$(jq -r '.updateTime' weather_data.json)
sunrise=$(jq -r '.daily[0].sunrise' weather_data.json)
sunset=$(jq -r '.daily[0].sunset' weather_data.json)
temperature_max=$(jq -r '.daily[0].tempMax' weather_data.json)
temperature_min=$(jq -r '.daily[0].tempMin' weather_data.json)
wind_direction_day=$(jq -r '.daily[0].windDirDay' weather_data.json)
wind_direction_night=$(jq -r '.daily[0].windDirNight' weather_data.json)
weather_text_day=$(jq -r '.daily[0].textDay' weather_data.json)
weather_text_night=$(jq -r '.daily[0].textNight' weather_data.json)
moonPhase=$(jq -r '.daily[0].moonPhase' weather_data.json)
humidity=$(jq -r '.daily[0].humidity' weather_data.json)
precip=$(jq -r '.daily[0].precip' weather_data.json)
pressure=$(jq -r '.daily[0].pressure' weather_data.json)
uvIndex=$(jq -r '.daily[0].uvIndex' weather_data.json)

# 天气数据更新时间
today_updateTime="$updateTime"
#日出时间
time_sunrise="$sunrise"
#日落时间
time_sunset="$sunset"
#月相
today_moonPhase="$moonPhase"
#相对湿度
today_humidity="$humidity %"
#降水量
today_precip="$precip mm"
#气压
today_pressure="$pressure hPa"
#紫外线指数
today_uvIndex="$uvIndex"
#最高温度
max_temperature="$temperature_max ℃"
#最低温度
min_temperature="$temperature_min ℃"
#白天风向
winddirection_day="$wind_direction_day"
#夜晚风向
winddirection_night="$wind_direction_night"
#白天天气
day_weather_text="$weather_text_day"
#夜晚天气
night_weather_text="$weather_text_night"
# 删除临时文件
rm weather_data.json
#############天气信息#############
# 获取当前日期的年份
current_year=$(TZ=Asia/Shanghai date +'%Y')

#姓名1
name1="${7}"                                              #⑦ 姓名1(读取github入参)
#姓名1的生日日期（只支持1900年-2100年出生的阴历日期）注意如果你是一月初一生日就写1-1不要写01-01
name1_birthdate_yinli="${8}"                              #⑧ 姓名1的阴历生日(读取github入参)
# 将用户输入的阴历生日转换为阳历日期
grep "@${current_year}-${name1_birthdate_yinli}" ./scripts/notification/1900-2100.txt | awk -F'@' '{print $1}'| head -n 1 > date_of_birth_1

name1_birthdate=$(cat date_of_birth_1)

#临时删除数据
rm -rf date_of_birth_1


#姓名2
name2="${9}"                                             #⑨ 姓名2(读取github入参)
#姓名2的生日日期（只支持1900年-2100年出生的阴历日期）注意如果你是三月初九生日就写3-9不要写03-09
name2_birthdate_yinli="${10}"                            #10 姓名2的阴历生日(读取github入参)

# 将用户输入的阴历生日转换为阳历日期
grep "@${current_year}-${name2_birthdate_yinli}" ./scripts/notification/1900-2100.txt | awk -F'@' '{print $1}'| head -n 1 > date_of_birth_2

name2_birthdate=$(cat date_of_birth_2)

#临时删除数据
rm -rf date_of_birth_2


# 恋爱开始日期
birthdate="${11}"                                   #11  恋爱开始时间


# 宝宝出生日期
baby_birthdate="${12}"                          #12  宝宝出生日期

# 构造name1完整的生日日期（当前年份 + 生日日期）
full_name1_birthdate="$name1_birthdate"
# 构造name2完整的生日日期（当前年份 + 生日日期）
full_name2_birthdate="$name2_birthdate"


# 获取当前日期
current_date=$(TZ=Asia/Shanghai date +'%Y-%m-%d')
# 使用 'date' 命令将日期转换为秒级时间戳
birthday_timestamp1=$(TZ=Asia/Shanghai date -d "$full_name1_birthdate" +%s)
birthday_timestamp2=$(TZ=Asia/Shanghai date -d "$full_name2_birthdate" +%s)
current_timestamp=$(TZ=Asia/Shanghai date -d "$current_date" +%s)

# name1如果生日已经过去，则计算距离下一个生日的天数
if [[ $birthday_timestamp1 -lt $current_timestamp ]]; then
  next_birthday1="$((current_year + 1))-$name1_birthdate_yinli"
 grep "@${next_birthday1}" ./scripts/notification/1900-2100.txt | awk -F'@' '{print $1}'| head -n 1 > date_of_birth_1_1
 name1_birthdate1_1=$(cat date_of_birth_1_1)
 rm -rf date_of_birth_1_1
  next_birthday_timestamp1=$(TZ=Asia/Shanghai date -d "$name1_birthdate1_1" +%s)
  days1=$(( (next_birthday_timestamp1 - current_timestamp) / 86400 ))

else
  # name1生日尚未过去，则计算距离生日的天数
  days1=$(( (birthday_timestamp1 - current_timestamp) / 86400 ))

fi

# name2如果生日已经过去，则计算距离下一个生日的天数
if [[ $birthday_timestamp2 -lt $current_timestamp ]]; then
  next_birthday2="$((current_year + 1))-$name2_birthdate_yinli"
  grep "@${next_birthday2}" ./scripts/notification/1900-2100.txt | awk -F'@' '{print $1}'| head -n 1 > date_of_birth_1_2
  name2_birthdate2_2=$(cat date_of_birth_1_2)
  rm -rf date_of_birth_1_2
  next_birthday_timestamp2=$(TZ=Asia/Shanghai date -d "$name2_birthdate2_2" +%s)
  days2=$(( (next_birthday_timestamp2 - current_timestamp) / 86400 ))

else
  # name2生日尚未过去，则计算距离生日的天数
  days2=$(( (birthday_timestamp2 - current_timestamp) / 86400 ))

fi

# 使用 'date' 命令将恋爱开始日期转换为秒级时间戳
birthdate_timestamp=$(TZ=Asia/Shanghai date -d "$birthdate" +%s)
# 计算天数差
lovedays=$(( (current_timestamp - birthdate_timestamp) / 86400 + 1))

# 使用 'date' 命令将宝宝出生日期转换为秒级时间戳
baby_birthdate_timestamp=$(TZ=Asia/Shanghai date -d "$baby_birthdate" +%s)
# 计算天数差
fanfan_born_days=$(( (current_timestamp - baby_birthdate_timestamp) / 86400 + 1))

# 每日一句
# curl -s -o yiyan_data.json "https://v1.hitokoto.cn/?encode=js&select=%23hitokoto" --compressed --header "Accept-Charset: UTF-8"
# 使用sed提取文本内容
# extracted_text=$(cat yiyan_data.json | sed -n 's/.*var hitokoto="\([^"]*\)".*/\1/p')

# 删除临时一言文件数据
# rm -rf yiyan_data.json

# 每日一句英文

curl -s -o OneDayEnglish.json "https://api.oioweb.cn/api/common/OneDayEnglish" --compressed --header "Accept-Charset: UTF-8"
# 使用jq提取文本内容
OneDayEnglish_yingyu=$(cat OneDayEnglish.json | jq -r '.result.content')
OneDayEnglish_hanzi=$(cat OneDayEnglish.json | jq -r '.result.note')

# 删除临时每日英语数据
rm -rf OneDayEnglish.json


content="今天是: $(TZ=Asia/Shanghai date +'%Y年%m月%d日')<br>地区：${city}<br>天气数据更新时间：${today_updateTime}<br>日出时间：${time_sunrise}<br>日落时间：${time_sunset}<br>月相：${today_moonPhase}<br>白天天气：${day_weather_text}<br>夜晚天气：${night_weather_text}<br>最高气温：${max_temperature}<br>最低气温：${min_temperature}<br>相对湿度：${today_humidity}<br>降水量：${today_precip}<br>气压：${today_pressure}<br>紫外线指数：${today_uvIndex}<br>白天风向：${winddirection_day}<br>夜晚风向：${winddirection_night}<br>今天是我们恋爱❤️的：第${lovedays}天<br>今天是${name1}出生❤️的：第${fanfan_born_days}天<br>距离${name1}的生日🍰还有：${days1}天<br>距离${name2}的生日🍰还有：${days2}天<br>今日英语：《${OneDayEnglish_yingyu}<br>${OneDayEnglish_hanzi}》"
template="html"

# echo "${content}"

# 构造请求 URL
url="https://www.pushplus.plus/send"

# 发送请求
curl --data-urlencode "token=$token" --data-urlencode "title=$title" --data-urlencode "content=$content" --data-urlencode "template=$template" --data-urlencode "topic=$topic"  "$url"
