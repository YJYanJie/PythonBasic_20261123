"""
    演示了函数
"""

"""
# 需求:向控制台打印 2*3 的 *,没有封装函数
# 直接打印
print("***")
print("***")

# 打印两次 2*3 的*,没有封装函数
# 循环实现
rows = 2
while rows > 0:
    print("*" * 3)
    rows -= 1
print("~~~" *10)
# 向控制台打印 2*3 的*
rows = 2
while rows > 0:
    print("*" * 3)
    rows -= 1

# 打印两次 2*3 的*,封装函数
def print_star():
    rows = 2
    while rows > 0:
        print("*" * 3)
        rows -= 1

# 函数调用
print_star()
print("~~~" * 10)
print_star()
"""

# 先打印一次 2*3 的*,再打印一次 1*4 的*
def print_star(rows, cols):
    while rows > 0:
        print("*" * cols)
        rows -= 1

print_star(2,3)
print("~~~" * 10)
print_star(1,4)
