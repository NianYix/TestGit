import requests
import os

'''https://ci.xiaohongshu.com/ 这个是小红书无水印拼接链接，后面只要传入：traceId 里面的参数即可'''
# 网站学习链接
# https://blog.csdn.net/wenxuhonghe/article/details/120142928
def fetchUrl(url):
    '''
    发起网络请求，获取网页源码
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ',
        'cookie':'smidV2=202205181406359eae90431fa3c555cbc77b3f49551dd500cb69a9c3b691490; gid.sig=Dogn49bZRQArsYJX4Gp9RgSSVvfl5EGIm8D9WPDJDyE; gid.ss=gSMQ9UOnDuZwH2oRGJG6BW6e4grs67TaYpnrW+8Wmd0Rp+LQcsgH6ccVKYanhBrd; xhsTrackerId=9f6eb54b-a086-4640-c6e2-a94d85b3f8ef; webBuild=1.0.20; a1=18561f525f7vyr6013x91eaiz0r81ytwitz696evf00000259995; webId=b9b05f3dbdc5e45d7800b05fc3465b9a; gid=yY2Kyi2JYf3DyY2Kyi2J29KdiWhvFK8yqCjyuhid03u8FK88Yyv9Ej888J2jjj28fYqDDiW8; gid.sign=JleUiJvt6LdGUyBt05G+1D0CAz0=; web_session=030037a49dc0b2f0011b8ad2d6244a5e79c9b6; xhsTracker=url=noteDetail&searchengine=baidu; timestamp2=1672387092104f721b64d924a054dd78e934eb0cf011bdb7bb5fa08271a7a94; timestamp2.sig=tJqf4boA9T7VFQ7LqjEvf6YSSM3JSXe1UbT8Kgyyvhk; extra_exp_ids=h5_1208_exp3,h5_1130_exp2,ios_wx_launch_open_app_exp,h5_video_ui_exp3,wx_launch_open_app_duration_origin,ques_exp1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    }
    
    r = requests.get(url, headers = headers)
    return r.text

def parsing_link(html):
    '''
    解析html文本，提取无水印图片的 url
    '''

    beginPos = html.find('imageList') + 11
    endPos = html.find(',"cover"')
    imageList = eval(html[beginPos: endPos])
#     print(imageList)
    for i in imageList:
        picUrl = f"https://ci.xiaohongshu.com/{i['fileId']}"
        yield picUrl, i['fileId']

def download(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    }

    with open(f'{filename}.jpg', 'wb') as v:
        try:
            r = requests.get(url, headers=headers)
            v.write(r.content)
        except Exception as e:
            print('图片下载错误！')

if __name__ == '__main__':
    original_link = 'https://www.xiaohongshu.com/discovery/item/60a5f16f0000000021034cb4'
    html = fetchUrl(original_link)
#     print(html)
    for url, fileId in parsing_link(html):
        print(f"download image {url}")
        download(url, fileId)
        
    print("Finished!")
