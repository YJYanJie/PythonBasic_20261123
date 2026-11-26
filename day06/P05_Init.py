"""
    演示了 init 方法
"""
class Person:
    home = "earth"

    def __new__(cls, *args, **kwargs):
        print("__new__方法被调用了")
        return object.__new__(cls)

    def __init__(self, name, age):
        print("__init__方法被调用了")
        self.name = name
        self.age = age

    def eat(self):
        print("eating")

# 创建类的实例
zs = Person("zs", 19)
zs.eat()