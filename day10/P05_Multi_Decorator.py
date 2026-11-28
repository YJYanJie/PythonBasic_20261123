"""
    演示了多层装饰器
"""
from math import sqrt

# 多层装饰器 语法糖模式,离函数近的装饰器先装饰,然后外面的装饰器再进行装饰
def get_abs(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner


def get_integer(f):
    def inner(x):
        x = int(x)
        return f(x)
    return inner

def func(x):
    return sqrt(x)

@get_integer
@get_abs
def func(x):
    return sqrt(x)

print(func("-4"))

"""
# 多层装饰器 手动调用形式
def get_abs(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner


def get_integer(f):
    def inner(x):
        x = int(x)
        return f(x)
    return inner

def func(x):
    return sqrt(x)

# 获取两个装饰器返回的函数对象
abs_inner = get_abs(func)
int_inner = get_integer(abs_inner)
# int_inner = get_integer(func)

print(int_inner("-4"))


# 以下调用顺序是错误的
# int_inner = get_integer(func)
# abs_inner = get_abs(int_inner)
"""
