#!/usr/local/bin/python
#coding=UTF-8

import re, fileinput

# 下面是有些无用的废代码
some_text = 'alpha. beta....gamma delta'
result = re.split('[. ]+', some_text)     ### 以任意长度的逗号和空格来分割字符串
print result     #### ['alpha', 'beta', 'gamma', 'delta']
print

# maxsplit参数表示字符串最多可以分割成的部分数
result2 = re.split('[. ]+', some_text, maxsplit=2)
print 'result2(maxsplit==2):', result2
result3 = re.split('[. ]+', some_text, maxsplit=1)
print 'result3(maxsplit==1):', result3
print

# findall以列表形式返回给定模式的所有匹配项
pat = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
result4 = re.findall(pat, text)
print 'result4(findall,a-z):', result4
pat = r'[..?\-",]+'
result5 = re.findall(pat, text)
print 'result5(findall,...):', result5
print

# 组对象匹配
m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
result6 = m.group(1)
print 'result6(group):', result6
print m.start(1),m.end(1),m.span(1)
print

### 找出email的发信人
pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
	m = pat.match(line)
	if m:
		print m.group(1)

### 可以这样来运行上面的代码：
### python filename message.eml