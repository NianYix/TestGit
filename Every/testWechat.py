import itchat
import requests
def get_response(msg):
 apiUrl = 'http://openapi.turingapi.com/openapi/api/v2'
 data = {
  'key': '180b4304b4b647d3b1920caf60f', # Tuling Key，API的值

  'info': msg, # 发出去的消息

  'userid': 'L1375124754', # 用户名
 }
 r = requests.post(apiUrl, data=data).json() # post请求

 return r.get('text')
@itchat.msg_register(itchat.content.TEXT) # 用于接收来自朋友间的对话消息 
def print_content(msg):
  print_content(msg);
  return get_response(msg['Text'])
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True) # 用于接收群里面的对话消息

def print_content(msg):

 return get_response(msg['Text'])
itchat.auto_login() # 通过微信扫描二维码登录
itchat.run()