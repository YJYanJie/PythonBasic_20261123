"""
    continue  break
"""
"""
# 打印0-9，跳过偶数
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
"""

# 求0-9每个数自己幂自己的加和，如果大于10000000则循环终止
sum = 0
for i in range(10):
    sum += i ** i
    print(f"第{i + 1}次循环的加和为{sum}")
    if sum > 10_000_000:
        break
print(sum)