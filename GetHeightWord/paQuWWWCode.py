import time
import requests
from lxml import etree
from multiprocessing.dummy import Pool
from requests.exceptions import RequestException
import openpyxl

def get_one_page(url):
    try:
        res = requests.get(url,headers = headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None
        
def parse_one_page(html):
    # 构造HTML解析器//*[@id="aspnetForm"]/div[6]/div[1]/div[3]/div[3]/div[1]/div
    info_list=[]
    ii_list  = html.xpath('//div[@class="kshdt"]//ul')
    for ii in ii_list:
        try:
            ##提取
            title = ii.xpath('./li/a/@title')[0].strip()
            sheet.append([title])
        except Exception:
            pass
       
def main(offset):
    # 构造主函数，初始化各个模块，传入入口URL
    base_url = 'https://www.chinca.org/CICA/Memberdynamics/List?p={}'
    url = base_url.format(offset)
    html = etree.HTML(get_one_page(url))
    parse_one_page(html)

if __name__ == '__main__':
    wb = openpyxl.Workbook()    # 获取工作簿对象
    sheet = wb.active           # 活动的工作表
    # 添加列名
    sheet.append(['title'])
    # 请求头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
           +'Chrome/62.0.3202.94 Safari/537.36'}
    # 使用线程池
    print('多线程爬取开始')
    start_time=time.time()
    p = Pool(8)
    p.map(main,[i for i in range(1,264)])
    # 保存位置
    wb.save(r'F:\Work\JerryStudy\Python\ZiLiao\Code\GetHeightWord\info.xlsx')
    #关闭线程池
    end_time=time.time()
    print('多线程爬取结束')
    print('耗时:',end_time-start_time)
    p.close()
    p.join()#用来等待进程池中的worker进程执行完毕，防止主进程在worker进程结束前结束。
