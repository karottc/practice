#!/usr/local/bin/python
#coding=UTF-8

from nntplib import NNTP
from time import strftime, time, localtime

day = 24 * 60 * 60 			# 一天的秒数

yesterday = localtime(time() - day)
date = strftime('%y%m%d', yesterday)
hour = strftime('%H%M%S', yesterday)

#servername = 'news.foo.bar'
servername = 'www.karottc.com'
group = 'com.lang.python.announce'
server = NNTP(servername)

ids = server.newnews(group, date, hour)[1]

for id in ids:
	head = server.head(id)[3]
	for line in head:
		if line.lower().startwith('subject:'):
			subject = line[9:]
			break

	body = server.body(id)[3]

	print subject
	print '-' * len(subject)
	print '\n'.join(body)

server.quit()