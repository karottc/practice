#!/usr/local/bin/python
#coding=UTF-8

print

# 生成器的方法
def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

r = repeater(42)
print r.next()
print r.send("Hello, world!")
print

def flatten(nested):
    result = []
    try:
        # 不要迭代器类似字符串的对象；
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result

# yield 的测试
def fun(n):
    for i in range(n):
        yield i **2

print list(fun(5))
t = fun(3)
print t.next()
print t.next()
print t.next()
#print t.next()      # 现在这句应该会返回一个StopIterator的异常，表明没有下一个元素了
print

def fab(max):
    a,b = 0,1
    i = 0
    while i < max:
        yield a
        a,b = b, a+b
        i += 1
f = fab(5)
print f.next()  # output: 0
print f.next()  # output: 1
print f.next()  # output: 1
print f.next()  # output: 2

for i in fab(10):
    print i, ',',
# output: 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 ,
print
print list(fab(10))
for i in list(fab(10)):
    print i, ',',
