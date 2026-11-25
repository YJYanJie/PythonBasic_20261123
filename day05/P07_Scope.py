"""
    演示了作用域
"""
a = int(10.0) # 全局, int:内建作用域(Python提供的内置函数)

def outer():
    a = 20 # 嵌套
    def inner():
        a = 30 # 局部
        print(a)
    return inner

f = outer()
f()