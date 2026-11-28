"""
    演示了类装饰器
"""
from math import sqrt

class ClassDecorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        x = abs(x)
        return self.f(x)

# @ClassDecorator
def func(x):
    """开根号"""
    return sqrt(x)

# print(func(-4))

# 创建类的实例
d = ClassDecorator(func)
print(d(-4))