"""
    练习题
    打印等腰三角形
"""
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))