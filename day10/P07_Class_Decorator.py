"""
    演示了类装饰器
    类装饰器区分：
        - 无参类装饰器：`__init__(self, func)`
        - 带参类装饰器：`__init__(self, 装饰器参数)`，`__call__(self, func)`
"""
from math import sqrt

""""""
# 不带参数的类装饰器
class ClassDecorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        x = abs(x)
        return self.f(x)

# @ClassDecorator
def func(x):
    # 开根号
    return sqrt(x)

# print(func(-4))

# 创建类的实例
d = ClassDecorator(func)
print(d(-4))


"""
# 带参数的类装饰器
class ClassDecorator:
    # __init__ 接受装饰器参数
    def __init__(self, param):
        self.param = param

    # __call__ 接受被装饰函数 + 执行包装逻辑
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"类装饰器接收到参数: {self.param}")
            ret = func(*args, **kwargs)
            return ret
        return wrapper

@ClassDecorator("test")
def foo():
    print("foo run")

foo()
"""