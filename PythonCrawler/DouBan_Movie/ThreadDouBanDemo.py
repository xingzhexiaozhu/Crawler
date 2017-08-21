# coding = utf-8

'''
使用多线程爬取电影
'''
import queue
import threading
from importlib import reload
import sys
from urllib import error
from urllib import request
import re
import time

reload(sys)
data = []
file_lock = threading._RLock
share_queue = queue.Queue()
thread_num = 3

class MyThread(threading.Thread):
    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()

def worker():
    global share_queue
    while not share_queue.empty():
        url = share_queue.get()
        my_page = get_page(url)
        find_title(my_page)
        time.sleep(1)
        share_queue.task_done()

def get_page(url):
    try:
        my_page = request.urlopen(url).read().decode("utf-8")
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError: the server couldn`t deal with the request")
            print("Error code: %s" % e.code)
        elif hasattr(e, 'reason'):
            print("URLError: failed to reach the server")
            print("Reason : %s" % e.reason)
    return my_page

def find_title(my_page):
    tmp_data = []
    movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', my_page, re.S)
    for index, item in enumerate(movie_items):
        if item.find("&nbsp") == -1:
            tmp_data.append(item)
    data.extend(tmp_data)

def main():
    global share_queue
    threads = []
    douban_url = "http://movie.douban.com/top250?start={page}&filter=&type="
    for index in range(10):
        share_queue.put(douban_url.format(page=index * 25))
    for i in range(thread_num):
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
        for thread in threads:
            thread.join()
            share_queue.join()
        with open("movie.txt", "w+") as my_file:
            print(data)
            for movie_name in data:
                my_file.write(movie_name + "\n")
        print("Spider successful!")

if __name__ == '__main__':
    main()