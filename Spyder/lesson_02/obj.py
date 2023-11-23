# 用type查看对象类型
print(type([1, 2, 3, 4]))
print(type('abcd'))
print(type({1:2, 2:3}))

# 用dir查看属性和方法
print(dir(list))

class Clazz(object):
    # self参考C++的this指针！
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # 声明成员函数的时候，第一个参数一定是self，不要忘记！
    def display(self):
        print(self.x, self.y)

print(type(Clazz))
clz = Clazz(100, 200)
clz.display()  # => display(clz)
        
class Base:
    def run(self):
        print('Base::run')

class Tom(Base):
    def run(self):
        print('Tom::run')

t = Tom()
print(isinstance(t, Base))
t.run()

def run(runner):
    runner.run()

class R1:
    def run(self):
        print('R1::run')

class R2:
    def run(self):
        print('R2::run')

run(R1())
run(R2())
