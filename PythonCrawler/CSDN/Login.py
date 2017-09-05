# coding = utf-8

# 方法一：直接请求
# from urllib import request
#
# # 目标网址
# url = "http://www.zhihu.com"
#
# # 直接请求
# response = request.urlopen(url)
#
# # 获取请求的状态码，200表示成功
# # 读取内容
# if(response.getcode() == 200):
#     print(response.read())


# 方法二：使用Request添加http header、data等数据
from urllib import request

# 目标网址
# url = "http://www.zhihu.com"
#
# # 需要添加的数据
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
#
# # 创建Request对象
# req = request.Request(url, headers=header)
#
# # 发送请求
# res = request.urlopen(req)
#
# # 获取请求的状态码，200表示成功
# # 读取内容
# if(res.getcode() == 200):
#     print(res.read())

# 方法三：cookie登录
import urllib
import re
from urllib import request
import http.cookiejar

# 目标网址
url = 'https://passport.csdn.net'

# 创建cookie容器
cookie = http.cookiejar.CookieJar()

# 创建一个opener
opener = request.build_opener(request.HTTPCookieProcessor(cookie))

# 添加http header
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]

# 需要封装的数据
h = opener.open(url).read().decode("utf8")
pattern1 = re.compile(r'name="lt" value="(.*?)"')
pattern2 = re.compile(r'name="execution" value="(.*?)"')
b1 = pattern1.search(h)
b2 = pattern2.search(h)
post_data = {
    'username':'610402400@qq.com',
    'password':'zl19921013',
    'lt': b1.group(1),
    'execution': b2.group(1),
    '_eventId': 'submit',
}
post_data = urllib.parse.urlencode(post_data).encode('utf-8')

# 使用带cookie的urllib访问网页
res = opener.open(url, post_data)
# text = res.read().decode('utf-8')
# print(text)

res2 = opener.open('http://my.csdn.net/my/mycsdn')
text2 = res2.read().decode('utf-8')
print(text2)
