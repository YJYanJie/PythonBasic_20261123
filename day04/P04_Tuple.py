"""
    演示了元组
"""
# 创建元组对象
# tup1 = (1, 2, 3)
# print(tup1, type(tup1))
# 当元组只有一个元素时,那么元素后面需要加 ,
# tup2 = (5,)
# print(tup2, type(tup2))

# 可以使用推导式方式创建元组对象
# 列表推导式
# list1 = [i*2 for i in range(5)]
# print(list1, type(list1))

# 元组推导式
# 注意: 这里创建的生成器对象
# tup1 = (i*2 for i in range(5))
# print(tup1, type(tup1))
# print(tuple(tup1))

# 元组的切片操作
# tup1 = (100, 200, 300, 400, 500)
# print(tup1[2])
# print(tup1[-3])
# print(tup1[:2])

# 元组相加
# tup1 = (100, 200, 300)
# tup2 = ("a", "b", "c")
# print(tup1 + tup2)

# 元组乘法
# print(tup1 * 3)

# 检查成员是否是元组的元素
# tup1 = (100, 200, 300, 400, 500)
# print(300 in tup1)

# 获取元组长度、最大值、最小值、加和
# print(len(tup1))
# print(max(tup1))
# print(min(tup1))
# print(sum(tup1))

# 遍历元组
# 直接遍历
# for item in tup1:
#     print(item)

# 通过索引遍历
# for idx in range(len(tup1)):
#     print(tup1[idx])

# 通过获取下标和值
# for i, item in enumerate(tup1):
#     print(i, item)

# 元组的不可变
tup1 = (100,200,300)

tup2 = (400,)
print(tup1, id(tup1))

tup1 = tup1 + tup2
# tup1 += tup2
print(tup1, id(tup1))