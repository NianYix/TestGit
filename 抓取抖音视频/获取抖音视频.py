import requests as req
import json
# https://blog.csdn.net/phpwechat/article/details/109353893
# 获取token值

def get_douyin_video(content):
    api = 'https://api.qingdou.vip/miniApp/watermark/index'
    params = {
        'val': content,
        '_platform': 'miniapp',
        'token': '更改为自己的 token'
    }
    data = req.post(api, headers=None, data=params, verify=False).text
    data = json.loads(data)
    return data['result']['url']


url = get_douyin_video('抖音口令')
print(url)