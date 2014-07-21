#!/usr/local/bin/python
#coding=UTF-8
__metaclass__=type
print

class FooBar:
    def __init__(self):
        print 'init function'
        self.somevar = 42

    def __del__(self):
        print 'del FooBar class'

f = FooBar()
print f.somevar
print

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah....'
            self.hungry=False
        else:
            print 'NO thanks.!'
    def __del__(self):
        print 'del Bird class'

class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound = 'Squawk!!'
    def sing(self):
        print self.sound
    def __del__(self):
        print 'del SongBird class'

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
print

def checkIndex(key):
    """
    所给的键能接收索引吗？
    未能被接受，键应该是一个非负的整数，如果它不是一个整数，
    会引发TypeError; 如果是负数，会引发IndexError,因为序列是无限长的。
    """
    if not isinstance(key, (int, long)):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        初始化算数序列
        起始值——序列中的第一个值
        步长——两个相邻值之间的差别
        改变——用户修改的值的字典
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        Get an item from arithmetic sequence
        """
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        """
        修改算数序列中的一个项
        """
        checkIndex(key)
        self.changed[key] = value
    def __del__(self):
        print 'del ArithmeticSequence class'

s = ArithmeticSequence(1,2)
print s[4]
s[4] = 2
print s[4]
print s[5]
print


class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
    def __del__(self):
        print 'del CounterList class'

cl = CounterList(range(10))
print cl
print cl.counter
print

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    def __del__(self):
        print 'del Rectangle class'

r = Rectangle()
r.width = 10
r.height = 5
print r.getSize()
r.setSize((150,100))
print r.getSize()
print

class MyClass:
    @staticmethod
    def smeth():
        print 'This is a static method'

    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls

MyClass.smeth()
MyClass.cmeth()
print

# 迭代器
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print f
        break
print

# 从迭代器得到序列
class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti = TestIterator()
list(ti)
print

# 一般生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1,2],[3,4],[5,6]]
for num in flatten(nested):
    print num
print
print list(flatten(nested))
print

# 递归生成器
def flatten_v2(nested):
    try:
        for sublist in nested:
            for element in flatten_v2(sublist):
                yield element
    except TypeError:
        yield nested
# 改进版本2
def flaten_v3(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten_v3(sublist):
                yield element
    except TypeError:
        yield nested
print
