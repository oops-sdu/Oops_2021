# -*- coding:utf-8 -*-
import codecs
from os import path

import jieba
#from scipy.misc import imread
from matplotlib.pyplot import imread
from wordcloud import WordCloud
import pandas as pd

# 这个函数暂时没有用到
def get_all_keywords(file_name):
    word_lists = []  # 关键词列表
    jieba.enable_parallel(8)
    with codecs.open(file_name, 'r', encoding='utf-8') as f:
        Lists = f.readlines()  # 文本列表
        for List in Lists:
            cut_list = list(jieba.cut(List))
            for word in cut_list:
                word_lists.append(word)
    word_lists_set = set(word_lists)  # 去除重复元素
    word_lists_set = list(word_lists_set)
    length = len(word_lists_set)
    print( u"共有%d个关键词" % length)
    information = pd.read_csv('tianqizhizi.csv')
    world_number_list = []
    word_copy=[]
    for w in word_lists_set:
        if (len(w) == 1):
            continue
        if (word_lists.count(w) > 3):
            world_number_list.append(word_lists.count(w))
            word_copy.append(w)
    information['key'] = word_copy
    information['count'] = world_number_list
    information.to_csv('sun_2.csv')


# 绘制词云
def save_jieba_result():
    # 设置多线程切割
    file_userdict = 'userdict.txt'  # 此处文件名为用户自定义的文件名，内容为不想被分开的词
    jieba.load_userdict(file_userdict)
    jieba.enable_parallel(4)
    dirs = path.join(path.dirname(__file__), '../pjl_comment.txt')
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()
    cut_text = " ".join(jieba.cut(comment_text))  # 将jieba分词得到的关键词用空格连接成为字符串
    with codecs.open('pjl_jieba.txt', 'a', encoding='utf-8') as f:
        f.write(cut_text)


def draw_wordcloud2():
    dirs = path.join(path.dirname(__file__), 'pjl_jieba.txt')
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()
    #print(comment_text)
    color_mask = imread("template.png")  # 读取背景图片

    # stopwords = [u'就是', u'电影', u'你们', u'这么', u'不过', u'但是', u'什么', u'没有', u'这个', u'那个', u'大家', u'比较', u'看到', u'真是',
    #              u'除了', u'时候', u'已经', u'可以',u'在',u'了',u'的',u'是',u'就',u'但',u'也',u'让我',u'让人',u'他',u'对',u' 都',u'和',u'我']
    stopwords = {}.fromkeys([line.rstrip() for line in open('stopword.txt')])
    cloud = WordCloud(font_path="simsun.ttc", background_color='white',
                      max_words=2000, max_font_size=200, min_font_size=4, mask=color_mask, stopwords=stopwords)
    word_cloud = cloud.generate(comment_text)  # 产生词云
    word_cloud.to_file("pjl_cloud.jpg")


save_jieba_result()
get_all_keywords('pjl_jieba.txt')
draw_wordcloud2()
