#coding=UTF-8
__author__ = 'karottc'

import urllib2

# urllib2_test01.py的另一个版本

"""
urllib2用一个Request对象来映射你提出的HTTP请求。
在它最简单的使用形式中你将用你要请求的地址创建一个Request对象，
通过调用urlopen并传入Request对象，将返回一个相关请求response对象，
这个应答对象如同一个文件对象，所以你可以在Response中调用.read()。
"""
req = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(req)
the_page = response.read()
# print the_page

import urllib
# 模拟登录CSDN
values = {"username":"karotte","password":"xxxxx"}
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
headers = {"User-Agent":user_agent,'Referer':'http://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn','lt':'LT-19313314-QkOACRq0dor4pkxKsabivp4y15Nhzg','execution':'e1s1','_eventId':'submit','Origin':'http://passport.csdn.net','Host':'passport.csdn.net'}
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
# print response.read()

# CSDN 登录不了，试试登录知乎, 知乎也不行，有动态验证码
values["username"] = "karottc@163.com"
values["password"] = "xxxxxxx"
url = "http://www.zhihu.com/#signin"
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
headers["Referer"] = "http://www.zhihu.com/"
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
print response.read()