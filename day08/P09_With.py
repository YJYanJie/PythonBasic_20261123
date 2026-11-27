"""
    演示了 with 自动释放资源
"""
from typing import final

# file = open("test.txt", "wt") # TextIOWrapper
# print(type(file))
"""
try:
    file = open("test.txt", "wt")
    file.write(str1)
    file.close()
finally:
    print("文件是否关闭", file.closed)
"""

"""
# 对 try 中的代码进行资源释放
try:
    try:
        file = open("test.txt", "wt")
        file.write(str1)
    finally:
        file.close()
finally:
    print("文件是否关闭", file.closed)
"""


"""
# 使用 with 的方式进行释放, 上下文管理对象
try:
    with open("test.txt", "wt") as file:
        file.write("hello world")
finally:
    print("文件是否关闭", file.closed)
"""

# 上下文管理器的实现
class MyContext:
    def __enter__(self):
        print("==== 调用 __enter__：获取资源 ====")
        return "我是enter返回的值"


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("==== 调用 __exit__：释放资源 ====")
        print(f"异常类型：{exc_type}")
        print(f"异常信息：{exc_val}")
        # return True  # 如果打开这一行，代码块里的异常会被屏蔽

with MyContext() as res:
    print("with内部代码块运行")
    print(f"as拿到的值：{res}")
    # a = 1 / 0   # 放开这行制造异常，你会发现 __exit__ 照样执行

print("with结束之后")
