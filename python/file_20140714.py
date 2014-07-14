#!/usr/local/bin/python
#coding=UTF-8

"""
f = open('somefile.txt','w')
f.write('Hello, ')
f.write('world !')
f.close()
"""

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'wordcount:',wordcount

def process(string):
	print 'Processing: ', string

f = open(filename)
char = f.char(1)
while char:
	process(char)
	char = f.read(1)
f.close()

f = open(filename)
while True:
	char = f.read(1)
	if not char: break
	process(char)
f.close()

# 处理行和上面类似
f = open(filename)
while True:
	line = f.readline()
	if not line: break
	process(line)
f.close()

# 不带参数的read方法：读取整个文件
f = open(filename)
for char in f.read():
	process(char)
f.close()

f = open(filename)
for line in f.readlines():
	process(line)
f.close

# 懒惰行迭代
import fileinput
for line in fileinput.input(filename):
	process(line)

f = open(filename)
for line in f:
	process(line)
f.close()