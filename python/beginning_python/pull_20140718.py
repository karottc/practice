#!/usr/local/bin/python
#coding=UTF-8

import socket, select

s = socket.socket()
host = socket.gethostname()
port = 1024
s.bind((host,port))

fdmap = {s.fileno():s}

s.listen(5)
p = select.poll()
p.register(s)
while True:
	events = p.poll()
	for fd,event in events:
		if fd in fdmap:
			c,addr = s.accept()
			print 'Got connection from:',addr
			p.register(c)
			fdmap[c.fileno()] = c
		elif event & select.POLLIN:
			data = fdmap[fd].recv(1024)
			if not data: 		# 没有数据，关闭连接
				print fdmap[fd].getpeername(),'disconnected'
				p.unregister(fd)
				del fdmap[fd]
		else:
			print data