class url_manager(object):
    # URL管理器中维护两个集合
    def __init__(self):
        # 待爬取的url集合
        self.new_urls = set()
        # 已爬取的url集合
        self.old_urls = set()

    # 向管理器中添加一个新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器中批量添加urls
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断待爬取列表是否有待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 从待爬取的集合中获取一个需要爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
