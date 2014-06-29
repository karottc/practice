#!/usr/local/bin/python
#coding=UTF-8

print

# 阶乘: n*(n-1)*(n-2)···3*2*1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# 幂: x^n
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print factorial(6)
print power(3,3)
print

# 二元查找
def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)

seq = [34,67,8,123,4,100,95]
seq.sort()
print seq
print search(seq,34,0,len(seq)-1)
print search(seq,100,0,len(seq)-1)
print
