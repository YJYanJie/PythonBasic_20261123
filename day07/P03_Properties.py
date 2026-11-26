"""
    演示了property
"""
"""
# @property 装饰器:将一个方法转换为属性来调用,转换后可直接使用 .方法名 来使用,无需使用 .方法名()
class Person:

    @property
    def eat(self):
        print("eating")

p = Person()
# p.eat()
p.eat
"""

"""
# Java 语言的处理方式,属性系优化,提供公开的 get-set 方法去获取以及设置属性的值
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        if self.__age >= 18:
            return 18
        return self.__age

zsh = Person("zsh", 60)
print(zsh.name)
# print(zsh.__age)
print(zsh.get_age())
zsh.set_age(18)
print(zsh.get_age())
"""

# Python 语言的处理
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        if self.__age >= 18:
            return 18
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    # @property装饰的方法不要和变量重名，否则可能导致无限递归。
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

p1 = Person("zsh", 60)
# print(p1.get_age())
print(p1.age)
# p1.name()
# p1.age = 15
# print(p1.age)