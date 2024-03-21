
# 微信小程序：高级健康Pro签到+完成日常任务
# 功能：签到获取G金，可以兑换物品和红包抵用券
# cron：一天运行1次就行，不放心运行2次
# 抓包：https://api.gaojihealth.cn/fund/api/ 找到userId和authorization。authorization包含"bearer "的头
# 变量：wx_gjjkpro_uid（填入userId）
#      wx_gjjkpro_bearer（填入authorization）
# 多账号：每个变量内用&进行分割，uid和bearer对应填写
# 范例：wx_gjjkpro_uid='账号1_userId&账号2_userId'
#      wx_gjjkpro_bearer='账号1_authorization&账号2_authorization'

import os
import requests

auth_tokens = []
user_ids = []
outmessage = ''
Num = 1

# 通知模块
def send_notification_message(title):
    try:
        from notify import send  # 导入青龙通知文件

        # 调用 send 函数发送通知
        send(title, ''.join(all_print_list))
    except Exception as e:
        if e:
            print('发送通知消息失败！')
            
# 调用青龙变量模块
def get_env():
    global auth_tokens
    global user_ids
    env_str = os.getenv("wx_gjjkpro_uid")
    if env_str:
        user_ids += env_str.replace("&", "\n").split("\n")
    env_str = os.getenv("wx_gjjkpro_bearer")
    if env_str:  # 添加了缺失的条件检查
        auth_tokens += env_str.replace("&", "\n").split("\n")
get_env()
# print(auth_tokens)
# print(user_ids)
# 设置请求URL
Qiandaourl = "https://api.gaojihealth.cn/gulosity/api/dkUserEvent/everyDaySign"
Renwuurl = "https://api.gaojihealth.cn/gulosity/api/dkUserEvent/browsePageCompleteTaskEvent"
# 任务列表
taskLists = [{ "browsePageId": "100004", "browsePageUrl": "/modules/integral/integral-mall/index", "taskId": 729 }, { "browsePageId": "100015", "browsePageUrl": "/modules/storeEmployeeQRcode/index?pageType=1", "taskId": 730 }, {"browsePageId":"100015","browsePageUrl":"/modules/benefit-card/details/freeca?itemId=75592395179481363&businessId=81363","taskId":656}]
# 任务执行循环
for auth_token, user_id in zip(auth_tokens, user_ids):
        # 准备请求头部
    headers = {
        "Connection": "keep-alive",
        "Content-Length": "61",
        "X-XSRF-TOKEN": "b2d71a88-1bf9-4268-9340-5ad5500295fd",
        "Authorization": auth_token,
        "siteId": "miniprogram",
        "grantType": "gj_app_auth",
        "channelPrice": "",
        "biz-market": "undefined",
        "from-channel": "gjjk_pro",
        "lastStart": "1256",
        "biz-identity": "undefined",
        "source": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
        "usign": "oWMs41NA1OWwX4zBTvkUuFvfWS-c",
        "Content-Type": "application/json;charset=UTF-8;",
        "shareId": "",
        "xweb_xhr": "1",
        "client-id": "miniprogram",
        "from-channelv2": "gjjk_pro",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wx73ec617ea0a6c8e8/1109/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    data = {
        "businessId": 81363,
        "userId": user_id,
        "taskId": 372
    }
    # 发送签到POST请求
    response = requests.post(Qiandaourl, headers=headers, json=data, verify=False)
    if response.status_code == 200:
        print("请求成功，已正常响应")
        outmessage += f'请求成功，已正常响应\n'
        Qiandao_date = response.json()
        Qiandaomessage = Qiandao_date['opMsg']
        outmessage += f'账户{user_id}签到结果：{Qiandaomessage}\n'
    # 输出响应内容
    # print(response.text)
    for m, taskList in enumerate(taskLists,1):
        response = requests.post(Renwuurl, headers=headers, json=taskList, verify=False)
        # print(response.text)
        X = response.text
        if X == 'true':
            print('签到成功')
            outmessage += f'第{m}个任务签到成功\n'
    informationurl = "https://api.gaojihealth.cn/fund/api/noauth/appCoupon/findDkSignActivityPage"
    params = {
        "businessId": "81363",
        "userId": user_id,
        "version": "1.4 "
    }
    headers_2 = {
    "Connection": "keep-alive",
    "X-XSRF-TOKEN": "2d6654f9-11c4-4f76-975e-2ebdb4f2e6d0",
    "Authorization": auth_token,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/9079",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx73ec617ea0a6c8e8/1109/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    # 省略的头部字段已经被注释掉，实际使用时根据需要添加
}
    response = requests.get(informationurl, headers=headers_2, params=params, verify=False)
    data = response.json()
    coins = data['integralResponse']['currentFund']
    outmessage += f'第{Num}个账户运行完毕,账户G金[{coins}]\n=================\n'
    Num += Num
print(outmessage)

# 发送消息内容
all_print_list = outmessage

# 调用函数发送通
send_notification_message(title='高济健康PRO小程序签到')