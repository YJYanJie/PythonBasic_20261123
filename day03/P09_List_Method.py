"""
    列表常用方法
"""
list1 = [1, 4, 2, 3, 4]
# list.insert(index,x)	在指定位置插入x
# list1.insert(1, 4)

# list.append(x)	在列表末尾追加x
# list1.append(4)

# list2 = [4, 5, 6]
# list1.extend(list2)	在列表1的末尾追加列表2的数据
# 创建新的对象
# print(list1 + list2)
# 直接在 list1 上进行追加
# list1.extend(list2)

# del list[index]	删除指定位置的数据或切片
# del list1[1]
# del list1[0:2]

# list.remove(x)	删除第一次出现的x
# list1.remove(1)

# list.pop([index])	删除指定位置的数据，默认为末尾数据
# list1.pop()
# list1.pop(1)

# list.clear()	清空列表中元素
# list1.clear()

# list[index] = x	修改指定位置的数据
# list1[1] = 10

# list1[start:end] = list2	修改列表切片的数据
# list1[1] = [1, 2, 3]

# sorted(list[,reverse=True])	返回排序后的新列表，可选降序
# list1 = sorted(list1, reverse=False) # 默认为 False, 即升序

# list.sort([reverse=True])	对列表就地排序，可选降序
# list1.sort() # 默认升序
# list1.sort(reverse=True)

# list.reverse()	反转列表中的元素
# list1.reverse()
# print(list1[::-1])

# list.index(x[,start,[,end]])	返回x在列表中首次出现的位置，可指定起始和结束范围
# print(list1.index(4))
# print(list1.index(4, 2))

# list.count(x)	返回x的数量
# print(list1.count(4))

# len(list)	返回列表元素个数
# print(len(list1))

# max(list)	返回列表中最大值
# print(max(list1))

# min(list)	返回列表中最小值
# print(min(list1))

# sum(list)	返回列表中所有元素和
# print(sum(list1))

# list.copy()	拷贝列表
# list2 = list1 # 未创建新对象
# list2 = list1[:] # 创建了一个新的对象
# list2 = list1.copy()  # 创建了一个新的对象
# print(id(list1), id(list2))

# list(x)	将序列转换为列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
zipped = zip(list1, list2)
print(type(zipped))
l3 = list(zipped)
print(l3, type(l3))

# print(list1)