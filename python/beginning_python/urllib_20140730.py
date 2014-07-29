#!/usr/local/bin/python
#coding=UTF-8

from urllib import urlopen

import re

p = re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
website = 'https://www.python.org/community/jobs'

p2 = re.compile('<a .*? href=(.*?)>(.*?)</a>')
website2 = 'http://www.karottc.com/'

p3 = re.compile('<h3 id="(.*?)"> (.*?) </h3>')
website3 = 'http://www.karottc.com/blog/2014/06/15/current-doing/'

text = urlopen(website).read()
for url, name in p.findall(text):
	print '%s (%s)' % (name, url)
print
print '======================================================'
text2 = urlopen(website2).read()
for url, name in p2.findall(text2):
	print 'name =', name
	print 'url =', url
	print
	print
### 只有这个text2有输出，正在研究中正则表达式ing........

print
print '======================================================'
text3 = urlopen(website3).read()
for url, name in p3.findall(text3):
	print 'name =', name
	print 'url =', url
	print
	print
