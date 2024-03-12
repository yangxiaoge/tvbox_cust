#!/bin/bash
#############版权信息#################
# 本脚本作者：bruce
# 版本：V1.0
# 日期：2023年12月14日
#############版权信息#################

result=$(
# 替换以下内容即可

# 浏览器获取步骤： 找到对应请求-右键-复制-全部复制为cURL(bash)
##############################
curl 'https://02290857.dotunnel01.xyz/user/checkin' \
-X 'POST' \
-H 'authority: 02290857.dotunnel01.xyz' \
-H 'accept: application/json, text/javascript, */*; q=0.01' \
-H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
-H 'cache-control: no-cache' \
-H 'content-length: 0' \
-H 'cookie: crisp-client%2Fsession%2Fa31cf4c2-8b4f-4655-b288-36b8089cb70e%2Fa46370a7-95af-3761-9079-d0c52134366d=session_2a25a5bc-83a8-481d-9cb8-2bd6515afdb2; crisp-client%2Fsession%2Fa31cf4c2-8b4f-4655-b288-36b8089cb70e=session_baebba4b-65bb-4f6c-8dcf-8239526e5306; crisp-client%2Fsession%2Fa31cf4c2-8b4f-4655-b288-36b8089cb70e%2Feee60fdd-0578-3f1e-8196-4a926a0ce65a=session_baebba4b-65bb-4f6c-8dcf-8239526e5306; cf_clearance=F.VMbYTIVyc4l1g4amIf3J8viF0UIeFsQqxfUg_M3C8-1708947529-1.0-AeKbTHBC+79RRaof+H1dDgsk3jbK7Fh7wdBEIqYvFNnFs3rkYRX1S7Fx75bj3VhZjHVXFYAaaOVBna1C/JbjNtM=; PHPSESSID=jap0hs8lkuttik6cudfaahmdfu; lang=zh-cn; uid=62186; email=yang.jianan0926%40gmail.com; key=959c4054713e87d2b89f8aee3c28c73e7bf762c873dee; ip=c9748cb45a1f5776d2a6808f94796965; expire_in=1740705104; mtauth=75a40beab43d3c320ffa0b287b028561' \
-H 'origin: https://02290857.dotunnel01.xyz' \
-H 'pragma: no-cache' \
-H 'referer: https://02290857.dotunnel01.xyz/user' \
-H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"' \
-H 'sec-ch-ua-mobile: ?0' \
-H 'sec-ch-ua-platform: "Windows"' \
-H 'sec-fetch-dest: empty' \
-H 'sec-fetch-mode: cors' \
-H 'sec-fetch-site: same-origin' \
-H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0' \
-H 'x-requested-with: XMLHttpRequest'
##############################

)
echo -en "请求结果:${result}"

keyWord="\"ret\":1"
if [[ $result == *$keyWord* ]]
then
    echo "签到成功！"
else
    echo "签到失败"
fi
