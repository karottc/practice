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
    print number,
print
for number in range(1,20):
    print number,
print
print

d = {'x':1,'y':2,'z':3}
for key in d:
    print key, 'correspond to', d[key]
print

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old'
print

print zip(names, ages)
print

combine = zip(names, ages)
for name, age in combine:
    print name, 'is', 'age', 'years old !'
print

# 列表推导式
girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']
result = [b+'+'+g for b in boys for g in girls if b[0] == g[0]]
print result
print
