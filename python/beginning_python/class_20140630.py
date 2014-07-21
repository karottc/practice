#!/usr/local/bin/python
#coding=UTF-8

print

# 自定义类
__metaclass__ = type
class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello, world! I'm %s." % self.name

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()
print

class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1,2,3])
s = SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','SPAM','SPAM','eggs','bacon','SPAM'])
print

class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print 'Hi, my value is',self.value

class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()
print
