with open('text.txt') as f:
    for line in f.readlines():
        print(line)

with open('text.txt', 'rb') as f:
    print(f.read())

s = 'abcdefg'
b = bytes(s)
print(b)

# 回去自己练习write函数写入
