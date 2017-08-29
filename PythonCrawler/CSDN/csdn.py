# coding=utf-8

# 对CSDN中的博客进行爬取，获取每篇博文的日期、主题、访问量、评论数量
import re
from urllib import request
import gzip

from bs4 import BeautifulSoup

class CSDNSpider:
    def __init__(self, pageIndex=1, url="http://blog.csdn.net/u012050154/article/list/1"):
        self.pageIndex = pageIndex
        self.url = url
        self.headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }

    # 求总页数
    def getPages(self):
        req = request.Request(url=self.url, headers=self.headers)
        res = request.urlopen(req)

        # 对抓取的CSDN内容进行解压操作
        data = res.read()
        data = ungzip(data).decode('utf-8')

        # 解析得到BeautifulSoup对象
        soup = BeautifulSoup(data, 'html5lib')
        pageNumText = soup.find('div','pagelist').span.get_text()
        # 209条  共14页
        pageNum = re.findall(re.compile(pattern=r'共(.*?)页'), pageNumText)[0]
        # print(pageNum)
        return pageNum

    # 设置要抓取的博文页面
    def setTargePage(self, index):
        self.url = self.url[0:self.url.rfind('/')+1]+str(index)

    # 读取博文信息
    def readData(self):
        ret = []
        req = request.Request(url=self.url, headers=self.headers)
        res = request.urlopen(req)

        # 对抓取的CSDN内容进行解压操作
        data = res.read()
        data = ungzip(data).decode('utf-8')

        # 解析得到BeautifulSoup对象
        soup = BeautifulSoup(data, 'html5lib')

        # 找到所有博文代码块
        items = soup.find_all('div', 'list_item article_item')
        for item in items:
            # 标题、链接、日期、阅读次数、评论个数
            title = item.find('span', 'link_title').a.get_text()
            link = item.find('span', 'link_title').a.get('href')
            writeTime = item.find('span', "link_postdate").get_text()
            readers = re.findall(re.compile(r'(.∗?)'), item.find('span', "link_view").get_text())[0]
            comments = re.findall(re.compile(r'(.∗?)'), item.find('span', "link_comments").get_text())[0]

        ret.append('日期：' + writeTime + '\t标题：' + title
                   + '\t链接：http://blog.csdn.net' + link
                   + '\t' + '阅读：' + readers + '\t评论：' + comments + '\n')
        return ret

def saveFile(data, index):
    path = "D:\\Program\\PythonCrawler\\CSDN\Data\\paper_" + str(index + 1) + ".txt"
    file = open(path, 'wb')
    page = '当前页：' + str(index + 1) + '\n'
    file.write(page.encode('gbk'))
    # 将博文信息写入文件(以utf-8保存的文件声明为gbk)
    for d in data:
        d = str(d) + '\n'
        file.write(d.encode('gbk'))
    file.close()

def ungzip(data):
    try:
        # print("正在解压缩...")
        data = gzip.decompress(data)
        # print("解压完毕...")
    except:
        print("未经压缩，无需解压...")
    return data


# 定义爬虫对象
csdn = CSDNSpider()

pageNum = int(csdn.getPages())
print("博客总页数：", pageNum)

for index in range(pageNum):
    csdn.setTargePage(index)
    print("当前页面：", index+1)

    papers = csdn.readData()
    saveFile(papers, index)