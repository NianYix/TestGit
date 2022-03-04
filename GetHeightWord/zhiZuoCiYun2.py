#@python 3.6.7
# -*- coding: utf-8 -*-

from os import path

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread
import jieba.analyse

CURRENT_PATH = path.dirname(path.abspath(__file__))
TEXT_FILE = path.join(CURRENT_PATH, 'test.txt')
IMG_FILE = path.join(CURRENT_PATH, 'a.png')
FONT_PATH = path.join(CURRENT_PATH, 'AliPuHui-Bold.ttf')


def get_frequencies():
    # use jieba to get Chinese frequencies
    # 'topK' is the max words need to return
    # 'withWeight=True' means return frequencies
    with open(TEXT_FILE, 'rb') as f:
        text = f.read()
    words = jieba.analyse.extract_tags(text, topK=200, withWeight=True)
    # words is list, change it to dict
    return dict(words)


def make_wordcloud(words):
    # get mask
    my_mask = imread(IMG_FILE)

    # set wordcloud
    my_wordcloud = WordCloud(
        font_path=FONT_PATH,
        background_color='white',
        mask=my_mask,
        max_font_size=68,
        min_font_size=8,
        contour_width=2,
        contour_color='steelblue'
    )
    # words must be dict
    my_wordcloud.generate_from_frequencies(words)

    return my_wordcloud


def show_it(wordcloud):
    # show it
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


def save_it(wordcloud, name):
    # save in current path
    filename = '{}.jpg'.format(name)
    wordcloud.to_file(path.join(CURRENT_PATH, filename))


if __name__ == '__main__':
    words = get_frequencies()
    wordcloud = make_wordcloud(words)
    show_it(wordcloud)
    save_it(wordcloud, 'my_wordcloud')
