#coding=UTF-8
__author__ = 'k'

import urllib2
import cookielib

# 声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieParocessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来创建opener
opener = urllib2.build_opener(handler)
# 此处的open方法通urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value

# 将cookie保存到文件
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
# 利用urllib2库的HTTPCookieParocessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来创建opener
opener = urllib2.build_opener(handler)
# 此处的open方法通urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.zhihu.com')
# 保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)