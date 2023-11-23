s = 'abcdefg'
try:
    str[0] = 'x'
except Exception as e:
    print(e)

# 修改字符串
li = list(s)
# print(li)
li[0] = 'x'
s = ''.join(li)
print(s)
s = '-'.join(li)
print(s)

# 切割
s = 'abc,def,ghi'
p1, p2, p3 = s.split(',')
print(p1, p2, p3)

# 下标访问和切片
s = 'abcdefg'
print(s[0], s[-1])
print(s[2:5])
