"""
    演示了闭包
"""
# 需求:在一个函数体中访问另一个函数体定义的变量
# n = 10
# while n > 0:
#     num = 10
#     n -= 1
# print(num)
"""
# 函数调用实现
def outer():
    a = 10
    b = 20
    c = 30
    inner(a)

def inner(a):
    print(a)

outer()
"""

def outer():
    a = 10
    def inner():
        print(a)
    return inner

f = outer()
print(f, type(f))
f()