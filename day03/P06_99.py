"""
    九九乘法表的实现
"""
# 外层循环控制行
for i in range(1, 10):
    # 内层循环控制每行的列
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()