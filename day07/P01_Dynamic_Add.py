"""
    演示了动态添加属性或者方法
"""
"""
# 动态的给对象添加实例属性
class Person:
    def __init__(self, name=None):
        self.name = name

p = Person("张三")
print(p.name)

p.age = 19
print(p.age)

p1 = Person("李四")
print(p1.age)


# 动态的给类添加类属性
class Person:
    def __init__(self, name=None):
        self.name = name

p = Person("张三")
print(p.name)

Person.home = "earth"
print(p.home)

p1 = Person("李四")
print(p1.home)


# 给实例添加普通方法
class Person:
    def __init__(self, name=None):
        self.name = name

    # 直接在类中定义普通方法,会有问题
    # def eat():
    #     print("eating")

def eat():
    print("eating")

p1 = Person("zs")
p1.eat = eat
p1.eat()


# 给实例添加实例方法
import types

class Person:
    def __init__(self, name=None):
        self.name = name

def eat(self):
    print(f"{self.name} is eating")

p1 = Person("zs")
# 将 eat 方法绑定到 p1 实例上
p1.eat = types.MethodType(eat, p1)
p1.eat()
# 方式2
# p1.eat = eat
# p1.eat(p1)


class Person:
    home = "earth"

    def __init__(self, name=None):
        self.name = name

# 定义类方法
@classmethod
def come_from(cls):
    print(f"来自{cls.home}")

# 定义静态方法
@staticmethod
def static_function():
    print("static function")

Person.come_from = come_from
Person.static_function = static_function

Person.come_from()
Person.static_function()

p = Person("zs")
del p.name
# print(p.name)
# del p
print(p)
"""

import types

class Person:
    # 限制类的实例能够添加的实例属性和实例方法
    # 但类属性, 类方法和静态方法还可以添加
    # __slots__ 仅对当前类生效,对子类无效
    __slots__ = ("name", "age", "eat", "weight")

    def __init__(self, name=None):
        self.name = name

def eat(self):
    print(f"{self.name}在吃饭")

def drink(self):
    print(f"{self.name}在喝水")

@classmethod
def class_method(cls):
    print("class method")

p = Person("张三")

# 添加实例属性
p.age = 10
print(p.age)  # 10

# 添加实例方法
p.eat = types.MethodType(eat, p)
p.eat()  # 张三在吃饭

# 添加实例属性
p.weight = 100  # AttributeError: 'Person' object has no attribute 'weight'

# 添加实例方法
# p.drink = type.MethodType(drink, p)  # AttributeError: type object 'type' has no attribute 'MethodType'

Person.class_method = class_method
Person.class_method()

