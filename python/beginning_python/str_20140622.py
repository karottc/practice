#!/usr/local/bin/python
#coding=UTF-8

# 格式化输出
print
# 元组转换需要用括号括起来
eq = '%s plus %s equals %s' % (1,1,2)
print eq
print

# 使用给定的宽度打印格式化后的价格列表
width = input('Please enter width: ')

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format_str = '%-*s%*.2f'

print '=' * width

print header_format % (item_width, 'Item', price_width, 'Price')

print '-' * width

print format_str % (item_width, 'Apples', price_width, 0.4)
print format_str % (item_width, 'Pears', price_width, 0.5)
print format_str % (item_width, 'Cantaloupes', price_width, 1.92)
print format_str % (item_width, 'Dried Apricots(16 oz.)', price_width, 8)
print format_str % (item_width, 'Prunes(4 lbs)', price_width, 12)

print '=' * width
