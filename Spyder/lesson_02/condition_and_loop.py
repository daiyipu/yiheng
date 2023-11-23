score = 80
if score > 90:
    print('A')
elif score > 70:
    print('B')
elif score >= 60:
    print('C')
else:
    print('D')

total = 0
i = 1
while i <= 100:
    total += i
    i += 1  # 没有++i或者--i
print(total)

'''
for循环只作用于容器！！！
没有这种写法：
  for (i = 0; i < 100; ++i):
      # TODO
上面这种循环只能用while实现
'''

i = 0
while i < 3:
    j = 0 
    while j <= 3:
        if j == 2:
            j += 1
            continue  # 又去了while j <= 3
        print(i, j)
        j += 1
    i += 1
