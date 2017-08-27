import urllib


class html_downloader(object):

    # 下载url对应的页面
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()

