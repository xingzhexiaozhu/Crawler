# coding=utf-8

# 分析豆瓣中最新电影的影评
import warnings
import jieba    #分词包
import re
from urllib import request

import numpy
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0,5.0)
from wordcloud import WordCloud # 词云包

# 获取最近上映的电影id和name的列表
def getLatestShowMovieList():
    resp = request.urlopen('https://movie.douban.com/cinema/nowplaying/beijing/')
    if resp.getcode() == 200:
        html_data = resp.read()
        soup = BeautifulSoup(html_data, 'html5lib')
        onShowMovie = soup.find_all('div',id='nowplaying')
        onShowMovieList = onShowMovie[0].find_all('li', class_='list-item')
        movieList = []
        for item in onShowMovieList:
            movieDict = {}
            movieDict['id'] = item['data-subject']
            movieDict['name'] = item['data-title']
            movieList.append(movieDict)
        return movieList
    else:
        print("Error Url!")

# 爬取电影的评论
def getCommentsById(movieId, pageNum):
    commentsList = []
    if pageNum > 0:
        start = (pageNum - 1) * 20
    else:
        return False
    reqUrl = 'https://movie.douban.com/subject/' + movieId + '/comments' +'?' +'start=' + str(start) + '&limit=20'
    req = request.urlopen(reqUrl)
    content = req.read()
    soup = BeautifulSoup(content, 'html5lib')
    commentList = soup.find_all('div', class_='comment')
    for item in commentList:
        commentsList.append(item.find('p').get_text().strip())
    return commentsList

# 爬虫程序启动
def main():
    # 循环获取第一个电影的前10页评论
    commentList = []
    movieList = getLatestShowMovieList()
    for i in range(10):
        commentListTmp = getCommentsById(movieList[0]['id'], i+1)
        commentList.append(commentListTmp)
    # 将列表中的数据转换为字符串
    comments = ''
    for comm in commentList:
        comments = comments + str(comm)
    # 使用正则表达式去除标点符号
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterData = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterData)
    # 使用结巴分词进行中文分词
    segment = jieba.lcut(cleaned_comments)
    words = pd.DataFrame({'segment':segment})
    # # 去掉停用词
    # stopwords = pd.read_csv("D:\Program\PythonCrawler\DouBan_Movie\stopword.txt",
    #                         index_col=False, quoting=3, sep="\t", names=['stopword'],
    #                         encoding='utf-8')  # quoting=3全不引用
    # words = words[~words.segment.isin(stopwords.stopword)]
    # 统计词频
    wordsFreq = words.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
    wordsFreq = wordsFreq.reset_index().sort_values(by=["计数"],ascending=False)
    #用词云显示
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)
    word_frequence = {x[0]: x[1] for x in wordsFreq.head(1000).values}
    word_frequence_list = []
    for key in word_frequence:
        temp = (key, word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud = wordcloud.fit_words(word_frequence_list)
    plt.imshow(wordcloud)

if __name__=="__main__":
    main()