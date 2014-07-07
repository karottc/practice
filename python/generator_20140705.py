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


