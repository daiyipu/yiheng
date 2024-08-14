class Person:
        # class attribute
    class_variable = "class variable"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_variable=str(self.name)+str(self.age)
        Person.class_variable=str(self.name)+str(self.age)+str(self.age)
 
    def show_info(self):
        print(f'name is {self.name}, {self.age} years old')
 
     # class method
    @classmethod
    def class_show_info(cls):
        print("I am a class method")

    @staticmethod
    def show_skill():
        print('walk, run, swim')
 
# 创建一个Person类的实例
person1 = Person('xiaoxiao', 20)
# 访问实例变量，输出：xiaoxiao 20
print(person1.name, person1.age)
# 访问实例方法，输出：name is xiaoxiao, 20 years old
person1.show_info()
# 访问静态方法，输出：walk, run, swim
person1.show_skill()
Person.show_skill()
Person.class_show_info()
person1.class_show_info()
print(Person.class_variable)
print(person1.class_variable)

# 继承

class Animal:
    def __init__(self, name):
        self.name = name
 
    def eat(self):
        print(self.name + " is eating...")
 
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
 
    def eat(self):
        print(self.breed + " eats more")
 
dog = Dog('Sky', 'Corgi')
# 覆盖父类方法，输出：Corgi eats more
dog.eat()
# 强制调用父类方法，输出：Sky is eating...
super(Dog, dog).eat()