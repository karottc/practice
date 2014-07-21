#!/usr/local/bin/python
#coding=UTF-8

print

# 输出9X9乘法表
title = '九九乘法表 by karottc'
width = 100
left_margin = (width - len(title)) / 2
print '+' + '-' * (left_margin-1) + ' ' + title + ' ' + '-' * (left_margin-1) + '+'
for a in range(1,10):
    print "|" + ' ' * 5,
    for b in range(1,a+1):
        print "%dx%d=%-2d" % (b,a,b*a),
    print ' ' * (width-3-6-1-7*a-1) + '|',
    print
print '+' + '-' * (width-5) + '+'
print
