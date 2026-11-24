"""
    演示了列表 list
"""
from pickletools import long1

# 创建列表对象
# list1 = [100, 200, 200, 300, 400, 500, 200]
# print(type(list1))

# 通过下标访问列表中的元素
# print(list1[1])
# print(list1[-4])

# 切片[起始:结束:步长]
# 取全部元素
# print(list1)
# 复制整个列表
# print(list1[:])
# 取索引从2开始到4(不包含)的元素
# print(list1[2:4])
# 取索引从2开始到末尾的元素
# print(list1[2:])
# 取索引从0开始到2(不包含)的元素
# print(list1[0:2])
# print(list1[:2])
# 取索引从2开始到-1(不包含)的元素
# print(list1[2:-1])
# 倒序取元素
# print(list1[::-1])


# 向列表中添加元素
# 向列表末尾追加元素
# list1.append(600)
# 向指定位置添加元素
# list1.insert(1, 300)
# print(list1)

# 列表相加
# list1 = [100, 200, 300]
# list2 = ["a", "b", "c"]
# print(list1 + list2)
# print(list1)

# 列表相乘
# print(list1 * 3)

# 修改列表中的元素
# list1[2] = 600
# print(list1)

# 通过切片修改多个值
# list1[1:3] = [600, 700, 800]
# print(list1)

# 检查对象是否是列表中
# print(200 in list1)

# 获取列表的长度
# print(len(list1))

# 获取列表中元素的最大值、最小值以及加和
# print(max(list1))
# print(min(list1))
# print(sum(list1))


# 列表的遍历
# 直接遍历
# for i in list1:
#     print(i)

# 通过下标遍历列表
# for idx in range(len(list1)):
#     print(list1[idx])

# 使用 enumrate() 同时获取列表的下标及元素
# for idx,item in enumerate(list1):
#     print(idx,item)

# 删除列表指定位置元素或者切片
# 删除列表中第一次出现的元素
# list1.remove(200)
# 删除指定的元素或者指定切片的元素
# del list1[1:3]

# list1 = [100, 200, 200, 300, 400, 500, 200]
# print(list1)
# reversed(list1) 是创建了一个新的集合,再新集合上进行遍历,但是 remove 的是 list1 原列表
# for item in reversed(list1):
#     print(item)
#     if item == 200:
#         list1.remove(item)
# for 循环中删除元素; 在其他编程语言中,不要在循环中调用可迭代对象的 remove 方法,而是使用可迭代器的删除方法
# for item in list1:
#     if item == 200:
#         list1.remove(item)
# print(list1)

# list2 = ["a", "b", "c", "d", "e", list1]
# print(list2)

# for item in list2[-1]:
#     print(item)

# 列表推导式
# for x in range(5):
#     print(x)

# list3 = [x * 2 for x in range(5)]
# print(list3)

list1 = [100, 200, 200, 300, 400, 500, 200]
# 带条件的列表推导式
list2 = [item for item in list1 if item != 200]
print(list2)

# list2 = []
# for item in list1:
#     if item != 200:
#         list2.append(item)
# print(list2)

# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
#
# list3 = [(i, j) for i in list1 for j in list2]
# print(list3)
# for i in list1:
#     for j in list2:
#         print(i, j)

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]

# zip 函数,可将多个可迭代对象对应元素打包为一个个元组
zipped = zip(list1, list2)
for item in zipped:
    print(item)