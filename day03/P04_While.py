"""
    while 循环
    需求:
        第 1 周有 2 只兔子,此后每周兔子的数量都增加上周数量的 2 倍,且期间没有兔子死亡, 求第 10 周共有多少只兔子;
"""
from time import sleep

week = 1
rabbit = 2

while week < 10:
    week += 1
    rabbit = rabbit + 2 * rabbit
    print(f"第{week}周兔子的数量是{rabbit}")
else:
    print("else语句的内容被执行了")
# print(f"第 {week} 周的兔子共有 {rabbit} 只")

"""
# 打印进度条
import time
num = 1
while num < 100:
    print("\r" + "=" * num, end="")
    time.sleep(0.2)
    # print(num)
    num += 1
"""
