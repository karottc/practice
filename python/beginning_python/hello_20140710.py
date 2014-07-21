#!/usr/local/bin/python
#coding=UTF-8

#print 'Hello world !'

def hello():
	print 'Hello world ! too'

# A test 
#hello()

def test():
	hello()
# 主程序中的__name__的值是__main__
if __name__ == '__main__':
	test()