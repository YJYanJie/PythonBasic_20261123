"""
    模块 my_add
"""
__all__ = ["num", "add", "_str1"]

num = 100
num1 = 200
_str1 = "123asd"
def add(a, b):
    return a + b

if __name__ == '__main__':
    print(__name__)
    print(add(10, 20))