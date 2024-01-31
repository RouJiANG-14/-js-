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
    # 定义用户信息
    user_ids = [ 919439334, 912694070, 912703596]

    # 每个用户运行的次数
    runs_per_user = 11

    # 定义请求的URL和Headers
    login_url =  'https://api.nblinks.cn/coreApi/user/consumer/v1/weChatAppLogin'
    signin_url = 'https://api.nblinks.cn/activityApi/points/v1/signin'
    task_url = 'https://api.nblinks.cn/activityApi/points/v1/task/finish'
    index_url = 'https://api.nblinks.cn/activityApi/points/v1/index'

    headers = {
        'charset': 'utf-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A7050 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160025 MMWEBSDK/20231105 MMWEBID/459 MicroMessenger/8.0.44.2502(0x28002C36) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wx69e931b913fc8e79/155/page-frame.html'
    }

    # 遍历用户列表，依次发送任务请求
    for user_id in user_ids:
        for _ in range(runs_per_user):
            # 发送登录的请求
            login_data = {
                "jsCode": '0b33X50w3f3GS13e6Z0w34OjRg23X50c',
                "appId" : 1000
            }
            send_post_request(login_url, headers, login_data)
            # 发送签到的请求
            signin_data = {
                "userId": user_id,
                "token": '2840973457b548ab92a8bc59c24e8265'
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
                "token": '2840973457b548ab92a8bc59c24e8265',
                "taskId": 1
            }
            send_post_request(task_url, headers, task_data)


            # 可以添加适当的延时，避免请求过于频繁
            time.sleep(0.5)  # 5秒延时，根据实际情况调整

        print(f"用户 {user_id} 完成 {runs_per_user} 次请求，等待切换到下一个用户")
        # 可以添加适当的延时，避免请求过于频繁
        time.sleep(0.5)  # 5秒延时，根据实际情况调整

if __name__ == "__main__":
    run_users()
