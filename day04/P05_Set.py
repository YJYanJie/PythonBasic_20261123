"""
    演示了集合
"""
# 创建集合对象
# set1 = {1, 2, 3}
# 将列表转换为集合,一般可用于去重场景
# set1 = set([1, 2, 3, 4, 3])
# print(set1)

# 定义一个空集合
# set1 = {}
# set1 = set()
# print(set1, type(set1))

# 通过集合推导式创建集合对象
# set1 = {i * 2 for i in range(10)}
# print(set1,type(set1))

# 向集合中添加元素
set1 = {1, 2, 3}
# set1.add(4)
# print(set1)

# 从集合中删除元素
# set1.pop()
# set1.pop()
# set1.remove(3)
# print(set1)

# 检查成员是否为集合中元素
# print(20 in set1)

# 获取长度、最大值、最小值、加和
# print(len(set1))
# print(max(set1))
# print(min(set1))
# print(sum(set1))

# 遍历集合
# for item in set1:
#     print(item)


# set常用方法
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# set.add(x)	添加元素
# set1.add(6)
# set1.add(set2)

# set.update(x)	添加元素，x可以为列表、元组、字符串、字典等可迭代对象
# set1.update("asd")

# set.union(x)	添加元素后返回一个新的集合，x可以为列表、元组、字符串、字典等可迭代对象
# set1.union(set2) # 创建了一个新的对象

# set.remove(x)	从集合中移除x，x不存在则报错
# set1.remove(1)

# set.discard(x) 	从集合中移除x，x不存在也不报错
# set1.discard(5)

# set.pop()	随机取出集合中的一个元素，如果集合为空则报错
# set1.pop()
# set.clear()	清空集合
# set1.clear()

# set.difference(x1,...)	求set1和x1的差集，返回一个新的集合
# print(set1.difference(set2))
# set.difference_update(x1,...)	求set1和x1的差集
# set1.difference_update(set2)

# set.intersection(x1,...)	求set1和x1的交集，返回一个新的集合
# print(set1.intersection(set2))
# set.intersection_update(x1,...)	求set1和x1的交集
# set1.intersection_update(set2)

# set1 & set2	两集合求交集
# print(set1 & set2)
# set1 | set2	两集合求并集
# print(set1 | set2)
# set1 - set2	两集合求差集
# print(set1 - set2)
# print(set2 - set1)

# set1.isdisjoint(set2)	判断两集合是否没有交集
# print(set1.isdisjoint(set2))
# set1.issubset(set2)	判断set1是否为set2的子集
# print(set1.issubset(set2))
# set1.issuperset(set2)	判断set2是否为set1的子集
# print(set1.issuperset(set2))

# set1.symmetric_difference(set2)	求两集合中不重复的元素，返回一个新的集合
# print(set1.symmetric_difference(set2))
# set1.symmetric_difference_update(set2)	求两集合中不重复的元素
# set1.symmetric_difference_update(set2)

# set.copy()	拷贝集合
# set3 = set1.copy()
# set3 = set1
# print(id(set1), id(set3))

# len(set)	返回集合元素个数
# max(set)	求集合中元素的最大值
# min(set)	求集合中元素的最小值
# sum(set)	求集合中元素的加和

print(set1)
