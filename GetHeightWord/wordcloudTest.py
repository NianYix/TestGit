import jieba
import wordcloud

txt = "Nick 是上海虹桥最帅的男人，没有之一，因为他就是最帅的"

w = wordcloud.WordCloud( width=1000,\
font_path="/Library/Fonts/Heiti.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")