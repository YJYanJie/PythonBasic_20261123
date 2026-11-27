"""
    演示了自定义异常
"""
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

def add(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    else:
        raise MyException("只能支持整数的加法计算")


try:
    res = add(1.0, 2)
except MyException as e:
    print(e.msg)
print(res)