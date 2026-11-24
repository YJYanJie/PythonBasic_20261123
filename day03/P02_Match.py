"""
    演示了 match 分支
    需求:给定月份,求该月有多少天
"""
from random import randint
# randint(a, b) -> [a,b] 之间的随机整数
m = randint(1, 20)

match m:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{m}月有31天")
    case 4 | 6 | 9 | 11:
        print(f"{m}月有30天")
    case 2:
        print(f"{m}月有28天")
    case _:
        print(f"输入的月份{m}不合理")