#!/usr/local/bin/python
#coding=UTF-8

print

name = ''
while not name or name.isspace():
    name = raw_input('Please enter your name: ')
    print 'Hello, %s !' % name
print

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    print number
print
