# python 面相对象编程

### 概述
我们将介绍Python的面向对象编程。面向对象编程（Object-Oriented Programming, 即OOP）是一种编程范型，它以对象为基础，将数据和操作封装在一个类（Class）中。在Python中，类是一种定义对象结构和行为的模板，而对象则是类的实例。类定义了一个新的类型，用于创建具有特定属性和方法的对象。类是面向对象编程的核心，它允许程序员使用对象来组织代码和复用代码。

### 类的定义
在Python中，类的基本语法如下：
``` {.line-numbers}
class ClassName:
    # class attribute
    class_variable = "class variable"
 
    def __init__(self, arg1, arg2):
        # instance variable
        self.instance_variable = arg1 + arg2
 
    # instance method
    def instance_method(self):
        print("I am an instance method")
 
    # class method
    @classmethod
    def class_method(cls):
        print("I am a class method")
 
    # static method
    @staticmethod
    def static_method():
        print("I am a static method")
```
下面逐一介绍上面示例代码中的各个元素。
    
1. *class ClassNam*e*：这是类定义的开始，以class关键字作为开头，ClassName是要定义的类的名称；最后面是冒号，冒号后面的内容需要缩进。

2. *class_variable = "class variable"*：这是类变量，它是一个在类中定义的全局变量，所有实例共享同一个变量。

3. *def __init__(self, arg1, arg2)*：这是类的构造函数，当一个类实例被创建时会自动调用。在这个例子中，构造函数接受两个参数：arg1和arg2。self是对当前实例的引用，调用时不需要写，由系统自动填入。构造函数可以不带参数，也可以带一个或多个参数。

3. *self.instance_variable = arg1 + arg2*：这是一个实例变量，每个实例都有自己独立的实例变量。在这个例子中，实例变量是arg1和arg2的和。

3. *def instance_method(self)*：这是一个实例方法，它需要一个实例作为其第一个参数（通常命名为self，也可以使用其他名称）。self是对当前实例的引用，调用时不需要写，由系统自动填入。

4. **@classmethod**：这是一个类方法装饰器，标识后面是一个类方法。它不需要实例作为其第一个参数，而是使用类名本身作为第一个参数（通常命名为cls，也可以使用其他名称）。cls是对当前类的引用，调用时不需要写，由系统自动填入。

5. **@staticmethod**：这是一个静态方法装饰器，标识后面是一个静态方法。它不需要实例或类作为其参数。


## 类的运算符重载
可以通过定义特定方法来重载类对象的运算符，以下是一些常见的运算符重载方法。
```{.line-numbers}
__add__(self, other)：重载加法运算符 +，用于实现两个对象的相加。
__sub__(self, other)：重载减法运算符 -，用于实现两个对象的相减。
__mul__(self, other)：重载乘法运算符 *，用于实现两个对象的相乘。
__truediv__(self, other)：重载除法运算符 /，用于实现两个对象的相除。
__floordiv__(self, other)：重载整数除法运算符 //，用于实现两个对象的整数相除。
__mod__(self, other)：重载取模运算符 %，用于实现两个对象的取模运算。
__pow__(self, other)：重载幂运算运算符 **，用于实现两个对象的幂运算。
__eq__(self, other)：重载相等运算符 ==，用于判断两个对象是否相等。
__ne__(self, other)：重载不等运算符 !=，用于判断两个对象是否不相等。
__lt__(self, other)：重载小于运算符 <，用于判断两个对象是否小于。
__le__(self, other)：重载小于等于运算符 <=，用于判断两个对象是否小于等于。
__gt__(self, other)：重载大于运算符 >，用于判断两个对象是否大于。
__ge__(self, other)：重载大于等于运算符 >=，用于判断两个对象是否大于等于。
```
假如我们定义了一个名为MyNumber的类，可以按照以下方式重载加法运算符。

***

## 继承
继承是一种实现面向对象编程的重要机制，它允许我们**基于已有的类创建新的类**，从而继承已有类的属性和方法。在Python中，使用class语句定义一个类时，可以在类名后面使用(base_classes)的形式指定该类要继承的父类。__*base_classes可以为一个类，也可以为多个类*__。多个类时，各个类之间用逗号进行分隔，属于多重继承的内容。
```{.line-numbers}
class Animal:
    def __init__(self, name):
        self.name = name
 
    def eat(self):
        print(self.name + " is eating...")
 
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Bird(Animal):
    def __init__(self, name, canfly):
        super().__init__(name)
        self.canfly=canfly

 
dog = Dog('Sky', 'Corgi')
# 输出：Sky is eating...
dog.eat()
# 输出：Corgi
print(dog.breed)
```
