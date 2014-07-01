#!/usr/local/bin/python
#coding=UTF-8

print

try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero !"
except TypeError:
    print "That wasn't a number, was it ?"
print

class MuffiedCalculator:
    muffied = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffied:
                print 'Division by zero is illegal !'
            else:
                raise

calculator = MuffiedCalculator()
print calculator.calc('10/2')
print
#calculator.calc('10/0')
#print
calculator.muffied = True
calculator.calc('10/0')
print


try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print x/y
except (ZeroDivisionError, TypeError, NameError), e:
    print "Your number were bogus..."
    print e
print

try:
    print "A simple task."
except:
    print "What? Something went wrong ?"
else:
    print "Ah...It went as planned."
print

while True:
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        value = x/y
        print 'x/y is', value
    except Exception, e:
        print "Invalid input:", e
        print "Please try again."
    else:
        break
print

x = None
try:
    x = 1/0
finally:
    print 'Cleaning up......'
    del x
print

try:
    1/0
except NameError:
    print 'Unknown variable'
else:
    print "That went well !"
finally:
    print "Cleaning up."
print

def faulty():
    raise Exception('Something is wrong')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print 'Exception handled'

ignore_exception()
print
handle_exception()
print
