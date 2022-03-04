from gevent import monkey; monkey.patch_all()
import requests
import gevent
import os
import re
import PySimpleGUI as sg
import sys
sys.path.append('..')
# sys.path.append(r'F:\Work\JerryStudy\Python\ZiLiao\Code') 
import entry
    


header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

root_path = ''

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)   

def crawling(path):
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    resp = requests.get(url=url, headers=header)
    heros = resp.json()['hero']
    index = 0
    task_list = []
    for hero in heros:
        index = index + 1

        heroId = hero['heroId']
        hero_url = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{heroId}.js'
        hero_resp = requests.get(url=hero_url, headers=header)
        skins = hero_resp.json()['skins']

        task = gevent.spawn(get_pic, skins,path)
        task_list.append(task)
        if len(task_list) == 10 or len(skins) == index:
            gevent.joinall(task_list)
            task_list = []
    


def get_pic(skins,path):
    for skin in skins:

        dir_name = skin['heroName'] + '_' + skin['heroTitle']
        pic_name = ''.join(skin['name'].split(skin['heroTitle'])).strip();
        url = skin['mainImg']
        
        if not url:
            continue 

        invalid_chars='[\\\/:*?"<>|]'
        pic_name = re.sub(invalid_chars,'', pic_name)
        download(dir_name, pic_name, url,path)

def download(dir_name, pic_name, url,path):
    print(f'{pic_name} 下载完成, {url}')
    dir_path = f'{path}\{dir_name}'
    mkdir(dir_path)
    
    resp = requests.get(url, headers=header)
    with open(f'{dir_path}\{pic_name}.png', 'wb') as f:
        f.write(resp.content)
    print(f'{pic_name} 下载完成')

def lol_main(path):
    root_path=path
    mkdir(path)
    crawling(path)
    
def entry_win():
    # 构建GUI
    layout_login = [[sg.Text('账号：'),sg.Input(key='account_id')],
                [sg.Text('密码：'),sg.Input(password_char='*', key='password')],
                [sg.Button('      确定      '), sg.Button('      关闭      ')]
                ]
    w = sg.Window('请输入账号密码', layout=layout_login)
    while True:
        event, values = w.read()
        if event in (None, '      关闭      '):
            sys.exit('程序关闭')
        # 判断账号密码
        elif values['account_id'] == 'admin' and values['password'] == '123':
            break
        else:
            sg.popup('账号密码不正确')
    w.close()
    
def get_filePath(callback):
    layout = [[sg.Text('选择结果存储地址')], [sg.Input(key='path',enable_events=True), sg.FolderBrowse('浏览')],
          [sg.Text('程序操作记录:',justification='center')],
          [sg.Output(size=(50, 8))],
          [sg.Button('   开始处理   '), sg.Button('      关闭      ')]]
    window = sg.Window('解析工具', layout)
    while True:
        event, values = window.read()
        if event in (None, '      关闭      '):
            break
        if event == '   开始处理   ':
            path = values['path']
            if os.path.exists(path):
                print('path:',path)
                callback(path)
                print('操作结束....')
            else:
                sg.popup('请选择正确的待处理文件及保存路径')
    window.close()

if __name__ == "__main__":
    entry_win()
    get_filePath(lol_main)
    
    
    