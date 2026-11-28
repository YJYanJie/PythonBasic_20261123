"""
    演示了装饰器
"""
from math import sqrt

def func(x):
    """求开根号"""
    return sqrt(x)

"""
# 装饰器设计模式
# 闭包实现装饰器,可以保留内层函数使用外层函数变量的状态
def decorator(func):
    count = 0
    def inner(x):
        # 添加额外功能
        nonlocal count
        print(count, "~~~~")
        count = count + 1
        x = abs(x)
        # 调用原始函数 func
        return func(x)
    # 返回内层函数对象
    return inner

inn = decorator(func)
print(inn(-4))
print(inn(-4))
print(inn(-4))

# print(func(-4))


# 同样可以实现功能,但是无法保存需要的状态
# 不清楚哪一个是函数对象,哪一个是函数对象需要的参数
# 装饰器语法糖不支持
# 装饰器版本返回的是函数,可以多次调用(函数的生命周期延长); 普通函数版本直接返回结果
def decorator(f, x):
    count = 0
    print(count, "~~~~")
    count = count + 1
    x = abs(x)
    return f(x)

print(decorator(func,-4))
print(decorator(func,-4))
"""

# 使用装饰器语法糖
def decorator(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

@decorator
def f(x):
    """求开根号"""
    return sqrt(x)


print(f(-4))