#!/usr/local/bin/python
#coding=UTF-8

print

# 全局变量

parameter = 'world'
def combine(parameter):
    print parameter + globals()['parameter']

combine('Hello')
print

x = y = 3
def change_global():
    global x
    y = 2
    z = 4
    x = x + y + z

change_global()
print x, y
