# coding=utf-8

from BaikePython import URLManager, HTMLDownloader, HTMLParser, HTMLOutput


# 爬虫总调度程序
class SpiderMain(object):
    # 构造函数初始化url管理器、HTML下载器、HTML解析器、输出四个对象
    def __init__(self):
        # url管理器
        self.urls = URLManager.url_manager()
        # url下载器
        self.downloader = HTMLDownloader.html_downloader()
        # url解析器
        self.parser = HTMLParser.html_parser()
        # 最终的输出
        self.outputer = HTMLOutput.html_output()

    # 爬虫调度程序
    def craw(self, root_url):
        count = 1
        # 添加入口URL
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 取出新的URL
                new_url = self.urls.get_new_url()
                # 下载该url对应的页面
                print("craw %d : %s" % (count, new_url))
                html_cont = self.downloader.download(new_url)
                # 解析该url对应的页面，得到新的链接和内容
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将新url添加到url管理器中
                self.urls.add_new_urls(new_urls)
                # 将解析到的内容收集起来
                self.outputer.collect_data(new_data)

                if count == 1000:  # 爬取1000个页面即可
                    break
                count = count + 1

            except:
                print("craw fail")
        # 最终输出爬取目标的内容
        self.outputer.output_html()


# 主函数启动爬虫
if __name__=="__main__":
    # root_url = "http://baike.baidu.com/item/Python/407313?fr=aladdin"
    root_url = "http://baike.baidu.com/item/Python"
    obj_Spider = SpiderMain()
    obj_Spider.craw(root_url)