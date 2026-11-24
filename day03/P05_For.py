"""
    演示了 for 循环
"""
# 遍历列表
for i in [10,20,30,40,50]:
    print(i)

# 遍历字符串
for a in "hello world":
    print(a)

# 遍历range数列
var = range(10)
print(type(var))

# range(start, stop[, step])
for i in range(1, 10, 2):
    print(i)
