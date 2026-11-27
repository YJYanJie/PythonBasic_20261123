"""
    演示了异常
"""
"""
# 语法错误
print("hello world)
# 异常: 变量未定义
print(var1)
"""

"""
# 没有对异常进行处理,如果除数为0,后面的代码都不会被执行
res = 10 / 0 # ZeroDivisionError: division by zero
print(res)
print("执行完毕")


# 异常处理
try:
    # 可能出现异常的代码部分
    res = 10 / 0
    print(res)
except:
    # 异常发生后,如何处理异常的代码
    print("除数不能为0")
print("执行完毕")
"""

"""
# 不同类型的异常可以有不同的处理方式
try:
    # res = 10 / 0
    print(res)
    # print("a" + 10)
# except ZeroDivisionError:
#     print("除数不能为0")
# except TypeError:
#     print("类型有问题")
# except NameError:
#     print("变量名未定义")
# except (NameError,TypeError) as e:
#     print(e)
except:
    print("other error")
"""

try:
    # 可能发生异常的代码
    res = 10 / 1
except:
    # 发生异常时,对异常进行处理的代码
    print("除数不能为0")
else:
    # 如果 try 中没有发生异常,将会执行 else 中的代码
    print(res)
