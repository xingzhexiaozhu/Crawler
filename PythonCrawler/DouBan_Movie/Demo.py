# coding = utf-8

from urllib import request

# 目标网址
url = "http://www.zhihu.com/"

# 请求
req = request.Request(url)

# 发送请求得到的响应
res = request.urlopen(req)

# 请求结果
data = res.read().decode("utf-8")

# 打印结果
# print(data)

# 请求得到的详细信息
# print(type(res))       # <class 'http.client.HTTPResponse'>
# print(res.geturl())      # https://www.zhihu.com/
# print(res.info())
print(res.getcode())