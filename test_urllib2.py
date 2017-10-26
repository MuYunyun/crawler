# 网页下载器和urllib2模块
#coding:utf-8
import urllib2
import cookielib

url = 'http://www.baidu.com'

print '第一种方法'
response1 = urllib2.urlopen(url) # 直接请求
print response1.getcode() # 获取状态码
print len(response1.read())

print '第二种方法(添加 data、http header)'
request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0') # 添加 http 的 header
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print '第三种方法(添加特殊情景的处理器)'
cj = cookielib.CookieJar() # 创建 cookie 容器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) # 创建 1 个 opener
urllib2.install_opener(opener) # 给 urllib2 安装 opener
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()