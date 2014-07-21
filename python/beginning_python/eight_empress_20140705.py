#!/usr/local/bin/python
#coding=UTF-8

import time

# nextX - 下一个皇后在水平线上的位置
# nextY - 下一个皇后在垂直线上的位置
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        # 水平距离为0 - 表示在同一垂直线上
        # 水平距离 == 垂直距离 - 表示在对角线上
        # 上面两种情况发生冲突
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num, state):
    if len(state) == num - 1 :
        for pos in range(num):
            if not conflict(state, pos):
                yield pos

print list(queens(4, (1,3,0)))

# 终于理解了这段代码啦
# 对于使用yield生成的迭代器(这种说法可能有些问题，但是就是那个意思吧)，每使用一次next方法，
# 就往下执行一个，不调用next方法，则不执行，而使用list 来遍历，则相当于调用了全部的next方法。
def queens2(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1 :
                yield (pos,)
            else:
                for result in queens2(num, state+(pos,)):
                    yield (pos,) + result

for solution in queens2(8):
    print solution
print len(list(queens2(8)))
print
print list(queens2(8))
print


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)
    for pos in solution:
        print line(pos)

import random

solution = random.choice(list(queens2(8)))
print solution
prettyprint(solution)
print

print '================calculate time cost======================='
start = time.time()
n = 16
len(list(queens2(n)))
print n,'个皇后耗时:',time.time()-start,'秒。'
print '================calculate time cost end==================='
# output:
# n = 8, costtime = 0.022351026535
# n = 9, costtime = 0.172093153
# n = 10, costtime = 0.523527145386
# n = 11, costtime = 2.75543093681
# n = 12, costtime = 15.839496851
# n = 13, costtime = 94.7705001831
# n = 14, costtime = 628.648396015
# n = 15, costtime = 4484.4150629
# n = 16, costtime = 