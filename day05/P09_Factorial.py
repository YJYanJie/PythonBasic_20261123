"""
    演示了函数递归
    需求:求一个整数的阶乘
"""
"""
# 循环实现
def get_factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
"""

# 递归实现
def get_factorial(n):
    # 递归结束条件
    if n == 1:
        return 1
    # 递归规律
    return n * get_factorial(n - 1)

print(get_factorial(5))