import PySimpleGUI as sg
import os

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