############ 富联e充微信小程序看视频得积分
############ 积分兑换1元充值抵用券
############ 每天运行脚本前需要手动点开小程序一次再运行

import requests
import json
import time

def send_post_request(url, headers, data):
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # 检查响应状态码
    if response.status_code == 200:
        print(f"请求成功")
        # 打印响应内容
        print(response.json())
    else:
        print(f"请求失败")
        # 打印错误信息
        print(response.text)

def run_users():
    ############################################## 定义用户信息 在这填入9位数字ID就行，多账号用“,”分割
    ############################################## 每天运行脚本前需要手动点开小程序一次再运行
    user_ids = [91943XXXX, 9126XXXXX, 91270XXXX]

    # 每个用户运行的次数
    runs_per_user = 11

    # 定义请求的URL和Headers
    signin_url = 'https://api.nblinks.cn/activityApi/points/v1/signin'
    task_url = 'https://api.nblinks.cn/activityApi/points/v1/task/finish'
    index_url = 'https://api.nblinks.cn/activityApi/points/v1/index'

    headers = {
        "Accept-Charset": "UTF-8",
        "referer": "https://2021003132662022.hybrid.alipay-eco.com/2021003132662022/0.2.2312121202.40/index.html#pages/pointsMall/pointsMall",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 11; zh-CN; SM-A7050 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.2.66 Mobile Safari/537.36 UCBS/3.22.2.66_230817192043 ChannelId(3) NebulaSDK/1.8.100112 Nebula AlipayDefined(nt:WIFI,ws:411|0|2.625) AliApp(AP/10.5.36.8100) AlipayClient/10.5.36.8100 Language/zh-Hans useStatusBar/true isConcaveScreen/true Region/CNAriver/1.0.0",
        "content-type": "application/json",
        "x-release-type": "ONLINE",
        "alipayMiniMark": "js7QhO/Yhj4Ig4A4OyJtv03e2S19mzl5zJ5O3j5PpmUzMSiB40V7eznAr9MO/84tVBtuCq67jcV4NIQAbSqbhCv5xCbZPtBwuskSfAd6KxM=",
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
    }

    # 遍历用户列表，依次发送任务请求
    for user_id in user_ids:
        for _ in range(runs_per_user):
            # 发送登录的请求
            signin_data = {
                "userId": user_id
            }
            send_post_request(signin_url, headers, signin_data)
            
            # 发送签到的请求
            index_data = {
                "userId": user_id
            }
            send_post_request(index_url, headers, index_data)

            # 发送任务请求
            task_data = {
                "userId": user_id,
                "taskId": 1
            }
            send_post_request(task_url, headers, task_data)

            # 可以添加适当的延时，避免请求过于频繁
            time.sleep(1)  # 5秒延时，根据实际情况调整

        print(f"用户 {user_id} 完成 {runs_per_user} 次请求，等待切换到下一个用户")
        # 可以添加适当的延时，避免请求过于频繁
        time.sleep(1)  # 5秒延时，根据实际情况调整

if __name__ == "__main__":
    run_users()
