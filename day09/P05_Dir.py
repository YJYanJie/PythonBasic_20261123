"""
    演示了dir函数
"""
"""
# 你将一个模块作为 dir() 的参数时，它会返回该模块中定义的名称列表，包括函数、类、变量等
import math
print(dir(math))
"""

"""
# 可以将一个对象作为 dir() 的参数,会返回该对象的属性和方法列表
class MyClass:
    home = "earth"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method(self):
        pass

obj = MyClass(1, 2)
print(dir(obj))
"""

"""
# 将类对象作为 dir 的参数
class MyClass:
    home = "earth"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method(self):
        pass
# 没有实例属性
print(dir(MyClass))
"""


def my_function():
    pass
variable = 10

print(dir())