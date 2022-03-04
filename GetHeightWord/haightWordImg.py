import jieba                                       # 调用jieba库
import matplotlib.pyplot as plt                    # 调用matplotlib库（通用设置）
plt.rcParams['font.sans-serif'] = 'SimHei'         # 设置正常显示符号
plt.rcParams['axes.unicode_minus'] = False
f_name = './test.txt'                          # line5到line22是高频词统计阶段，上篇有讲到过
with open(f_name, encoding='utf-8')as a:
    b = a.read()
words = jieba.lcut(b)
count = {}
for word in words:
    if len(word) < 2:
        continue
    else:
        count[word] = count.get(word, 0)+1
list1 = list(count.items())
list1.sort(key=lambda x: x[1], reverse=True)
list2 = []                                         # 用于储存10大高频词的所占比
for a in range(10):
    sun = 0.0
    for i in range(10):
        word, number = list1[i]
        print("关键字：{:-<10}频次:{:+>8}".format(word, number))
        sun = number+sun                          # 统计10大高频词的次数总和
    word, number = list1[a]
    list2.append(number/sun)
list3 = []                                        # 储存10大词汇
for b in range(10):
    word, number = list1[b]
    list3.append(word)
plt.title("高频词占比表")                           # 添加图表标题
plt.pie(x=list2, labels=list3, autopct='%.2f%%')    # 绘制扇形图
plt.show()                                          # 输出扇形图即可

