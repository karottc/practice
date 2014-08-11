#!/python/usr/local/bin
#coding=UTF-8

import re

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
