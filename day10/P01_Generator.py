"""
    演示了生成器对象的创建
"""
"""
# 方式1: 通过推导式创建生成器对象

from typing import Iterator
from collections.abc import Iterable

gen = (i for i in range(100))
print(gen, type(gen)) # <generator object <genexpr> at 0x0000023C011C5B40> <class 'generator'>

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# 判断是否是可迭代的 
print(isinstance(gen, Iterable))
# 判断是否是迭代器
print(isinstance(gen, Iterator))


# for i in gen:
#     print(i)
"""

"""
#方式2: 通过类似标准函数形式创建生成器对象
def fibo():
    a, b = 0, 1
    while True:
        # 生成器通过 yield 进行只的返回
        yield b
        a, b = b, a + b

f = fibo()
print(type(f)) # <class 'generator'>
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
"""

# 获取生成器函数的返回值
def fibo():
    a, b, count = 0, 1, 0
    while count < 10:
        # 生成器通过 yield 进行值的返回
        yield b
        a, b, count = b, a + b, count + 1
    return "65432321done123456"

f = fibo()
try:
    while True:
        print(next(f))
except StopIteration as e:
    print(e)