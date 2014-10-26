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
print the_page
