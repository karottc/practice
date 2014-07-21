#!/usr/local/bin/python
#coding=UTF-8

print

def hello(name):
    return 'Hello, ' + name + ' !'

print hello('world')
print

def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

print fibs(10)
print fibs(15)
print

def square(x):
    'Calculates the square of the number x'
    return x*x

print square.__doc__
print

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

storage = {}
init(storage)
print storage
print

def hello_2(greeting='Hello', name='world'):
    print '%s, %s!' % (greeting, name)

hello_2(greeting='Welcome to',name='the real world')
print
