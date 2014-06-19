#!/usr/local/bin/python
# coding=UTF-8

# 列表 以及 list函数等

var0 = ['aaa','bbb','ccc','ddd','eee']
del var0[2]
print var0
print

var1 = list('hello')
print var1
print

var2 = list('perl')
var2[2:] = list('ar')
print var2
print

var3 = [1,5]
var3[1:1] = [2,3,4]
print var3

var3[1:4] = []
print var3
print

var4 = list('helloworld!!!')
var4[1::3] = list('1234')
print var4
print

# 上面的输出结果为：
#['aaa', 'bbb', 'ddd', 'eee']
#['h', 'e', 'l', 'l', 'o']
#['p', 'e', 'a', 'r']
#[1, 2, 3, 4, 5]
#[1, 5]
#['h', '1', 'l', 'l', '2', 'w', 'o', '3', 'l', 'd', '4', '!', '!']

# 列表方法
var3.append(6)
print var3
print

var5 = [1,2,3]
var6 = [4,5,6]
var5.extend(var6)
print var5
print

var7 = [7,8,9]
print var6+var7
print var6
print
