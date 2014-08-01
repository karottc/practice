#!/usr/local/bin/python
#coding=UTF-8

from urllib import urlopen

import re

p = re.compile('<a href="http://yinwang\\.org/(.*?)">(.*?)</a>')
website = 'http://www.yinwang.org/'
text = urlopen(website).read()

"""
print
print '======================================================'

# 输出对应的每篇的blog标题和URL。
for url, name in p.findall(text):
	print 'name =', name
	print 'url = http://yinwang.org/%s' % url
	print
	print

print '======================================================'
"""
print
blogs = p.findall(text)
count = len(blogs)
print 'total count: %d pieces blog !' % count 
print

url_1 = 'http://yinwang.org/' + blogs[0][0]
name_1 = blogs[0][1]
url_2 = 'http://yinwang.org/' + blogs[1][0]
name_2 = blogs[1][1]

print 'First blog: %s - %s !' % (name_1, url_1)
print 'Second blog: %s - %s !' % (name_2, url_2) 
### 20140731: 
### total count: 54 pieces !
### First blog: Homeless！我需要你的帮助！ - http://yinwang.org/blog-cn/2014/07/30/help !
