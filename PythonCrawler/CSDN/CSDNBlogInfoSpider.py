# coding=utf-8

# 对CSDN博客信息进行爬取，获取博客的主题、链接、日期、访问量、评论数等信息

class CSDNSpider:
    def __init__(self, pageIndex=1, url="http://blog.csdn.net/u012050154/article/list/1"):
        self.pageIndex = pageIndex
        self.url = url
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }