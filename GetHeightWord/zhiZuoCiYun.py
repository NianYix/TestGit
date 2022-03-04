# 词云图
import jieba
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from collections import Counter
import PIL

df = pd.read_excel(r'F:\Work\JerryStudy\Python\ZiLiao\Code\GetHeightWord\info.xlsx')

def get_cut_words(content_series):
    # 读入停用词表
    stop_words = [] 

    with open(r"F:\Work\JerryStudy\Python\ZiLiao\Code\GetHeightWord\test.txt", 'rb') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())

    # 添加关键词
    my_words = ['5G', 'CPS', '高速公路', '人工智能', '数字孪生体','工业大数据','智能大数据']    
    for i in my_words:
        jieba.add_word(i) 

    # 自定义停用词
    my_stop_words = ["""'中国', '项目', '承建', '电建', '...','一个','集团'
                    '开工', '签署', '合同', '中标', '正式','协议', '首个',
                    '巴基斯坦', '印尼', '集团', '老挝', '国家','市场','首次','改造'"""
                    ]   
    stop_words.extend(my_stop_words)               

    # 分词
    content=';'.join([ str(c) for c in content_series.tolist()])
    word_num = jieba.lcut(content)

    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i)>=2]

    return word_num_selected

text1 = get_cut_words(content_series=df['title'])


from collections import Counter
c = Counter(text1)
common_c = c.most_common(300)
# common_c

# 读入图片
mask = np.array(PIL.Image.open(r'F:\Work\JerryStudy\Python\ZiLiao\Code\GetHeightWord\a.png'))
# 配置词云参数 
wc = WordCloud(
            # 设置字体
            font_path = r'F:\Work\JerryStudy\Python\ZiLiao\Code\GetHeightWord\AliPuHui-Bold.ttf',#必须加中文字体，否则格式错误
            # 设置背景色
            background_color='white',
            scale=5,  # 数值越大，图片越清晰，但是太大电脑可能会吃不消
            # 词云形状
            mask=mask,
            width=900, height=600,
            #max_words=300,            # 词云显示的最大词语数量
            max_font_size=60,         # 设置字体最大值
            min_font_size=3,         # 设置子图最小值
            random_state=50           # 设置随机生成状态，即多少种配色方案
            )
# 生成词云
wc.generate_from_frequencies(dict(common_c))
# 生成图片并显示
plt.imshow(wc)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file(r'F:\Work\JerryStudy\Python\ZiLiao\Code\GetHeightWord\pic.jpg')

